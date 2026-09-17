#!/usr/bin/env python
"""Módulo de consolidação e análise dos resultados da avaliação da RAG — TCC G26.

Este script lê exclusivamente em modo somente-leitura o arquivo
dataset/resultados_avaliacao.md, garantindo que nenhum dado original seja modificado.
Ele calcula métricas estatísticas e indicadores qualitativos para o TCC.

Uso via terminal:
    python dataset/consolidar_resultados.py
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
RESULTADOS_PATH = BASE_DIR / "resultados_avaliacao.md"
PERGUNTAS_PATH = BASE_DIR / "perguntas.json"


def carregar_avaliacoes(caminho: Path | None = None) -> list[dict[str, Any]]:
    """Lê e processa as 60 seções de perguntas de resultados_avaliacao.md em modo somente-leitura."""
    path = caminho or RESULTADOS_PATH
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    conteudo = path.read_text(encoding="utf-8")
    secoes = re.split(r"### (G\d{2}-Q\d{2}) \((pt|en)\)", conteudo)

    avaliacoes: list[dict[str, Any]] = []

    def _obter_campo(nome: str, texto: str) -> str:
        padrao = r"- \*\*" + re.escape(nome) + r":\*\* (.*)"
        m = re.search(padrao, texto)
        return m.group(1).strip() if m else ""

    def _obter_bloco_texto(campo: str, texto: str) -> str:
        padrao = r"- \*\*" + re.escape(campo) + r":\*\*\s*````(?:text)?\n(.*?)\n````"
        m = re.search(padrao, texto, re.DOTALL)
        if m:
            return m.group(1).strip()
        # Fallback para linha simples caso não haja bloco delimitado
        padrao_simples = r"- \*\*" + re.escape(campo) + r":\*\* (.*)"
        m_simples = re.search(padrao_simples, texto)
        return m_simples.group(1).strip() if m_simples else ""

    for i in range(1, len(secoes), 3):
        qid = secoes[i]
        lang = secoes[i + 1]
        bloco = secoes[i + 2]

        m_pergunta = re.search(r"\*\*Pergunta:\*\* (.*?)\n\*\*", bloco, re.DOTALL)
        pergunta = m_pergunta.group(1).strip() if m_pergunta else ""

        m_cat = re.search(r"\*\*Categorias:\*\* (.*)", bloco)
        categorias = (
            [c.strip() for c in m_cat.group(1).split("|")] if m_cat else []
        )

        m_exp = re.search(r"\*\*Expectativa:\*\* `(.*?)`", bloco)
        expectativa = m_exp.group(1).strip() if m_exp else ""

        m_grupo = re.search(r"- \*\*Nome do grupo:\*\* (.*)", bloco)
        grupo_nome = m_grupo.group(1).strip() if m_grupo else ""

        # Fontes obtidas
        fontes: list[str] = []
        m_fontes = re.search(
            r"- \*\*Fontes obtidas:\*\*\n(.*?)(?=\n- \*\*|\n###|$)", bloco, re.DOTALL
        )
        if m_fontes:
            for linha in m_fontes.group(1).split("\n"):
                linha_s = linha.strip()
                if linha_s.startswith("- "):
                    fontes.append(linha_s[2:].strip())

        nota_str = _obter_campo("Qualidade geral (1–5)", bloco)
        nota = int(nota_str) if nota_str.isdigit() else 0

        avaliacoes.append(
            {
                "id": qid,
                "language": lang,
                "group": int(qid[1:3]),
                "group_name": grupo_nome,
                "question": pergunta,
                "categories": categorias,
                "expected": expectativa,
                "resposta_rag": _obter_bloco_texto("Resposta obtida (RAG)", bloco),
                "resposta_sem_rag": _obter_bloco_texto("Resposta sem RAG", bloco),
                "fontes": fontes,
                "fonte_correta": _obter_campo("Fonte correta recuperada", bloco),
                "resposta_adequada": _obter_campo("Resposta adequada", bloco),
                "sinalizou_insuficiencia": _obter_campo("Sinalizou insuficiência", bloco),
                "qualidade": nota,
                "observacoes": _obter_campo("Observações", bloco),
            }
        )

    return avaliacoes


def calcular_metricas_gerais(avaliacoes: list[dict[str, Any]]) -> dict[str, Any]:
    """Calcula indicadores executivos sobre as avaliações."""
    total = len(avaliacoes)
    if total == 0:
        return {}

    notas = [q["qualidade"] for q in avaliacoes if q["qualidade"] > 0]
    media_qualidade = sum(notas) / len(notas) if notas else 0.0

    contagem_adequada = Counter(q["resposta_adequada"] for q in avaliacoes)
    contagem_notas = Counter(notas)

    # Subconjunto: perguntas no contexto (esperado 'context')
    contexto = [q for q in avaliacoes if q["expected"] == "context"]
    fc_sim = sum(1 for q in contexto if q["fonte_correta"] == "sim")
    fc_parcial = sum(1 for q in contexto if q["fonte_correta"] == "parcial")
    taxa_cobertura_fontes = (
        ((fc_sim + fc_parcial) / len(contexto)) * 100 if contexto else 0.0
    )
    taxa_fontes_estrita = (fc_sim / len(contexto)) * 100 if contexto else 0.0

    # Subconjunto: perguntas fora de contexto (esperado 'out_of_context')
    fora_contexto = [q for q in avaliacoes if q["expected"] == "out_of_context"]
    recusa_sim = sum(1 for q in fora_contexto if q["sinalizou_insuficiencia"] == "sim")
    taxa_recusa_segura = (
        (recusa_sim / len(fora_contexto)) * 100 if fora_contexto else 0.0
    )

    taxa_adequada = (
        (contagem_adequada.get("sim", 0) / total) * 100 if total > 0 else 0.0
    )

    return {
        "total_perguntas": total,
        "total_contexto": len(contexto),
        "total_fora_contexto": len(fora_contexto),
        "media_qualidade": round(media_qualidade, 2),
        "distribuicao_notas": dict(contagem_notas),
        "respostas_adequadas": dict(contagem_adequada),
        "taxa_adequada_pct": round(taxa_adequada, 1),
        "fontes_corretas_contexto": {
            "sim": fc_sim,
            "parcial": fc_parcial,
            "nao": len(contexto) - fc_sim - fc_parcial,
        },
        "taxa_cobertura_fontes_pct": round(taxa_cobertura_fontes, 1),
        "taxa_fontes_estrita_pct": round(taxa_fontes_estrita, 1),
        "recusa_segura_fora_contexto": {
            "sim": recusa_sim,
            "nao": len(fora_contexto) - recusa_sim,
        },
        "taxa_recusa_segura_pct": round(taxa_recusa_segura, 1),
    }


def calcular_metricas_por_grupo(
    avaliacoes: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Calcula estatísticas agregadas por grupo (1 a 10)."""
    grupos: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for q in avaliacoes:
        grupos[q["group"]].append(q)

    linhas_grupo = []
    for g in sorted(grupos.keys()):
        itens = grupos[g]
        nome = itens[0]["group_name"]
        notas = [x["qualidade"] for x in itens if x["qualidade"] > 0]
        media_q = sum(notas) / len(notas) if notas else 0.0

        total_g = len(itens)
        adeq_sim = sum(1 for x in itens if x["resposta_adequada"] == "sim")
        fc_sim = sum(1 for x in itens if x["fonte_correta"] == "sim")
        fc_parcial = sum(1 for x in itens if x["fonte_correta"] == "parcial")
        recusa_sim = sum(1 for x in itens if x["sinalizou_insuficiencia"] == "sim")

        in_ctx = sum(1 for x in itens if x["expected"] == "context")
        out_ctx = sum(1 for x in itens if x["expected"] == "out_of_context")

        linhas_grupo.append(
            {
                "group": g,
                "group_name": nome,
                "total": total_g,
                "in_context": in_ctx,
                "out_of_context": out_ctx,
                "media_qualidade": round(media_q, 2),
                "adequadas_sim": adeq_sim,
                "adequadas_pct": round((adeq_sim / total_g) * 100, 1),
                "fontes_sim": fc_sim,
                "fontes_parcial": fc_parcial,
                "recusa_sim": recusa_sim,
            }
        )
    return linhas_grupo


def calcular_robustez_linguistica(
    avaliacoes: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    """Calcula indicadores comparativos por categoria de ruído textual."""
    categorias = [
        ("correta", "Texto Limpo / Formal"),
        ("sem_pontuacao", "Pontuação Ausente/Excessiva"),
        ("emoji", "Presença de Emojis"),
        ("giria", "Gírias / Linguagem Informal"),
        ("erro_ortografia_pt", "Erros de Ortografia (PT)"),
        ("erro_ortografia_en", "Erros de Ortografia (EN)"),
        ("afirmacao", "Afirmações (Inversão Pragmática)"),
        ("sarcasmo", "Sarcasmo e Ironia"),
    ]

    resultado = {}
    for cat_key, rotulo in categorias:
        itens = [q for q in avaliacoes if cat_key in q["categories"]]
        if not itens:
            continue
        notas = [x["qualidade"] for x in itens if x["qualidade"] > 0]
        media_q = sum(notas) / len(notas) if notas else 0.0
        adeq_sim = sum(1 for x in itens if x["resposta_adequada"] == "sim")
        resultado[cat_key] = {
            "rotulo": rotulo,
            "total": len(itens),
            "media_qualidade": round(media_q, 2),
            "adequadas_sim": adeq_sim,
            "adequadas_pct": round((adeq_sim / len(itens)) * 100, 1),
        }
    return resultado


def imprimir_sumario_terminal(avaliacoes: list[dict[str, Any]]) -> None:
    """Imprime sumário executivo formatado no terminal para uso ágil."""
    m_geral = calcular_metricas_gerais(avaliacoes)
    grupos = calcular_metricas_por_grupo(avaliacoes)
    robustez = calcular_robustez_linguistica(avaliacoes)

    print("\n" + "=" * 76)
    print("      CONSOLIDAÇÃO DOS RESULTADOS DA AVALIAÇÃO DA RAG — TCC G26")
    print("=" * 76)
    print(f"Total de perguntas avaliadas: {m_geral['total_perguntas']} (100% preenchidas)")
    print(f"  • No contexto do curso (expected: context): {m_geral['total_contexto']}")
    print(f"  • Fora do contexto (expected: out_of_context): {m_geral['total_fora_contexto']}")
    print("-" * 76)
    print("INDICADORES CHAVE (KPIs):")
    print(f"  • Qualidade Geral Média:          {m_geral['media_qualidade']} / 5.0")
    print(f"  • Taxa de Resposta Adequada:      {m_geral['taxa_adequada_pct']}% ({m_geral['respostas_adequadas'].get('sim', 0)}/{m_geral['total_perguntas']})")
    print(f"  • Recuperação de Fonte Correta:   {m_geral['taxa_cobertura_fontes_pct']}% no contexto ({m_geral['taxa_fontes_estrita_pct']}% estrita)")
    print(f"  • Controle de Alucinação (Recusa): {m_geral['taxa_recusa_segura_pct']}% seguro nas fora de contexto")
    print(f"  • Distribuição de Notas (1 a 5):  {dict(sorted(m_geral['distribuicao_notas'].items()))}")
    print("-" * 76)
    print("DESEMPENHO POR GRUPO TEMÁTICO:")
    print(f"{'Grp':<4} | {'Nome do Grupo':<36} | {'Média':<5} | {'Adeq %':<7} | {'Fontes'}")
    print("-" * 76)
    for g in grupos:
        fontes_desc = f"{g['fontes_sim']} sim"
        if g["fontes_parcial"]:
            fontes_desc += f", {g['fontes_parcial']} parc."
        print(f"G{g['group']:02d} | {g['group_name']:<36} | {g['media_qualidade']:<5.2f} | {g['adequadas_pct']:<6.1f}% | {fontes_desc}")
    print("-" * 76)
    print("ROBUSTEZ LINGUÍSTICA E RESISTÊNCIA A RUÍDO:")
    for _, info in robustez.items():
        print(f"  • {info['rotulo']:<34} (N={info['total']:2d}) : Média {info['media_qualidade']:.2f} | Adequadas: {info['adequadas_pct']}%")
    print("=" * 76 + "\n")


def main() -> None:
    avaliacoes = carregar_avaliacoes()
    imprimir_sumario_terminal(avaliacoes)


if __name__ == "__main__":
    main()
