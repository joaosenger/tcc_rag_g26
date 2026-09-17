"""Dashboard Streamlit: Consolidação e Visualização da Avaliação da RAG — TCC G26.

Permite explorar graficamente os resultados, tabelas agregadas e inspecionar
as 60 perguntas individualmente com comparação lado a lado (Com RAG vs Sem RAG).

Execução:
    streamlit run dataset/app_resultados.py
"""
from __future__ import annotations

import sys
from pathlib import Path

# Adiciona o diretório dataset ao sys.path para importação de consolidar_resultados
DATASET_DIR = Path(__file__).resolve().parent
if str(DATASET_DIR) not in sys.path:
    sys.path.insert(0, str(DATASET_DIR))

import altair as alt
import pandas as pd
import streamlit as st
from consolidar_resultados import (
    calcular_metricas_gerais,
    calcular_metricas_por_grupo,
    calcular_robustez_linguistica,
    carregar_avaliacoes,
)

# Configuração da Página
st.set_page_config(
    page_title="TCC G26 — Resultados da Avaliação RAG",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilização CSS customizada para apresentação acadêmica
st.markdown(
    """
    <style>
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 16px;
        border-left: 5px solid #1f77b4;
        margin-bottom: 10px;
    }
    .badge-sim { color: #155724; background-color: #d4edda; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
    .badge-parcial { color: #856404; background-color: #fff3cd; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
    .badge-nao { color: #721c24; background-color: #f8d7da; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def obter_dados():
    avaliacoes = carregar_avaliacoes()
    m_geral = calcular_metricas_gerais(avaliacoes)
    m_grupos = calcular_metricas_por_grupo(avaliacoes)
    m_robustez = calcular_robustez_linguistica(avaliacoes)
    return avaliacoes, m_geral, m_grupos, m_robustez


avaliacoes, m_geral, m_grupos, m_robustez = obter_dados()

# Cabeçalho Principal
st.title("📊 Avaliação Experimental do Sistema RAG — TCC G26")
st.caption(
    "Pós-Graduação em Processamento de Linguagem Natural — UFG | Análise de Desempenho sobre o Corpus do Curso"
)
st.markdown("---")

# Linha de Indicadores Chave (KPIs)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total de Perguntas", f"{m_geral['total_perguntas']}", "100% auditadas")
with col2:
    st.metric("Qualidade Geral", f"{m_geral['media_qualidade']} / 5.0", "Média global")
with col3:
    st.metric("Assertividade", f"{m_geral['taxa_adequada_pct']}%", "56 de 60 adequadas")
with col4:
    st.metric(
        "Recuperação de Fontes",
        f"{m_geral['taxa_cobertura_fontes_pct']}%",
        f"{m_geral['taxa_fontes_estrita_pct']}% estrita",
    )
with col5:
    st.metric(
        "Controle de Alucinação",
        f"{m_geral['taxa_recusa_segura_pct']}%",
        "20 de 22 recusas seguras",
    )

st.markdown("")

# Seção de Metodologia e Escala de Avaliação
with st.expander("ℹ️ Metodologia Experimental: Organização dos Grupos e Critérios de Avaliação (1 a 5)", expanded=True):
    col_met1, col_met2 = st.columns([3, 2])

    with col_met1:
        st.markdown("#### 🎯 Divisão dos Grupos (10 Grupos × 6 Perguntas = 60 Total)")
        st.markdown(
            """
            As 60 perguntas foram estruturadas para avaliar tanto a **recuperação precisa no corpus** 
            (38 perguntas no contexto) quanto o **controle de alucinação** (22 perguntas deliberadamente fora de contexto):

            - **G01 — Perguntas diretas:** Recuperação objetiva de conceitos centrais (ex: *"O que é o pipx?"*).
            - **G02 — Longas e contextualizadas:** Compreensão de cenários detalhados e localização de tópicos específicos.
            - **G03 — Longas sem relação c/ material:** Avalia se o modelo recusa temas externos mesmo em prompts extensos.
            - **G04 — Diretas sem relação c/ material:** Controle estrito de alucinação em perguntas factuais externas (ex: *"Quem descobriu o Brasil?"*).
            - **G05 — Erros de ortografia:** Robustez a erros de digitação e desvios ortográficos em português e inglês.
            - **G06 — Erros de pontuação:** Resistência a pontuação ausente, repetida ou caótica (ex: *"???", ",,,"*).
            - **G07 — Emojis:** Robustez a símbolos gráficos e elementos não-semânticos no texto (🤖, 📚, 🚀, 🔐).
            - **G08 — Afirmações:** Interpretação pragmática de afirmações declarativas como pedidos de validação.
            - **G09 — Gírias:** Compreensão de linguagem informal e coloquialismos (*"de boa"*, *"fala aí"*).
            - **G10 — Sarcasmo e ironia:** Resiliência semântica e pragmática a formulações adversariais e retóricas.
            """
        )

    with col_met2:
        st.markdown("#### ⭐ Escala de Qualidade Geral (1 a 5)")
        st.markdown(
            """
            - **Nota 5 (Excelente):** Resposta precisa, concisa, totalmente ancorada no corpus e com fontes corretas (ou recusa segura perfeita).
            - **Nota 4 (Boa):** Resposta correta e fundamentada, apresentando pequenas verbosidades ou detalhes menores de formatação.
            - **Nota 3 (Regular):** Resposta parcialmente correta, incompleta ou com propagação de artefato (ex.: transcrição fonética de áudio).
            - **Nota 2 (Insuficiente):** Não atende ao objetivo central da pergunta ou força associação indevida com chunks irrelevantes.
            - **Nota 1 (Incorreta):** Resposta falsa, inventada ou enganosa (*0 ocorrências registradas*).

            ---
            **Legenda dos Indicadores:**
            - **Fonte Correta:** `sim` (top-1) | `parcial` (top-3) | `n/a` (nas 22 fora de contexto).
            - **Resposta Adequada:** `sim` | `parcial` | `não` (atendimento ao usuário).
            - **Sinalizou Insuficiência:** `sim` (esperado nas 22 fora de contexto para evitar alucinação).
            """
        )

st.markdown("")

# Estrutura de Abas
tab_graficos, tab_tabela, tab_explorador = st.tabs(
    [
        "📈 Gráficos & Visualizações",
        "📋 Tabela Agregada por Grupo",
        "🔍 Explorador das 60 Perguntas",
    ]
)

# -------------------------------------------------------------
# ABA 1: GRÁFICOS E VISUALIZAÇÕES
# -------------------------------------------------------------
with tab_graficos:
    st.subheader("Desempenho Visual por Dimensão")

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.markdown("##### 1. Qualidade Média por Grupo Temático (1 a 5)")
        df_grupos = pd.DataFrame(m_grupos)
        df_grupos["Grupo_Rotulo"] = df_grupos.apply(
            lambda r: f"G{r['group']:02d}: {r['group_name']}", axis=1
        )

        chart_grupos = (
            alt.Chart(df_grupos)
            .mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
            .encode(
                x=alt.X("media_qualidade:Q", title="Nota Média (1 a 5)", scale=alt.Scale(domain=[0, 5])),
                y=alt.Y("Grupo_Rotulo:N", sort=None, title="Grupo Temático"),
                color=alt.Color(
                    "media_qualidade:Q",
                    scale=alt.Scale(scheme="blues"),
                    legend=None,
                ),
                tooltip=[
                    alt.Tooltip("Grupo_Rotulo:N", title="Grupo"),
                    alt.Tooltip("media_qualidade:Q", title="Média", format=".2f"),
                    alt.Tooltip("adequadas_pct:Q", title="% Adequadas", format=".1f"),
                ],
            )
            .properties(height=350)
        )
        st.altair_chart(chart_grupos, use_container_width=True)

    with col_g2:
        st.markdown("##### 2. Distribuição das Notas de Avaliação (1 a 5)")
        dist_notas = m_geral["distribuicao_notas"]
        df_notas = pd.DataFrame(
            [
                {"Nota": f"Nota {nota}", "Quantidade": qtd, "Pct": f"{(qtd/60)*100:.1f}%"}
                for nota, qtd in sorted(dist_notas.items(), reverse=True)
            ]
        )

        chart_notas = (
            alt.Chart(df_notas)
            .mark_bar(color="#2ca02c", cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
            .encode(
                x=alt.X("Nota:N", sort=None, title="Nota Atribuída"),
                y=alt.Y("Quantidade:Q", title="Número de Perguntas"),
                tooltip=["Nota", "Quantidade", "Pct"],
            )
            .properties(height=350)
        )
        st.altair_chart(chart_notas, use_container_width=True)

    st.markdown("---")
    col_g3, col_g4 = st.columns(2)

    with col_g3:
        st.markdown("##### 3. Robustez a Ruídos Textuais e Linguísticos")
        df_robustez = pd.DataFrame(list(m_robustez.values()))

        chart_rob = (
            alt.Chart(df_robustez)
            .mark_bar(color="#ff7f0e", cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
            .encode(
                x=alt.X("media_qualidade:Q", scale=alt.Scale(domain=[0, 5]), title="Qualidade Média"),
                y=alt.Y("rotulo:N", sort="-x", title="Tipo de Ruído"),
                tooltip=[
                    alt.Tooltip("rotulo:N", title="Condição"),
                    alt.Tooltip("media_qualidade:Q", title="Nota Média", format=".2f"),
                    alt.Tooltip("adequadas_pct:Q", title="% Adequadas", format=".1f"),
                    alt.Tooltip("total:Q", title="Amostras"),
                ],
            )
            .properties(height=320)
        )
        st.altair_chart(chart_rob, use_container_width=True)

    with col_g4:
        st.markdown("##### 4. Taxa de Resposta Adequada (%) por Grupo")
        chart_adeq = (
            alt.Chart(df_grupos)
            .mark_bar(color="#1f77b4", cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
            .encode(
                x=alt.X("adequadas_pct:Q", scale=alt.Scale(domain=[0, 100]), title="Taxa Adequada (%)"),
                y=alt.Y("Grupo_Rotulo:N", sort=None, title="Grupo"),
                tooltip=["Grupo_Rotulo", "adequadas_pct", "media_qualidade"],
            )
            .properties(height=320)
        )
        st.altair_chart(chart_adeq, use_container_width=True)


# -------------------------------------------------------------
# ABA 2: TABELA AGREGADA POR GRUPO
# -------------------------------------------------------------
with tab_tabela:
    st.subheader("Tabela Resumo dos 10 Grupos Experimentais")
    st.markdown(
        "Esta tabela consolida os 10 grupos de teste (6 perguntas por grupo, totalizando 60 perguntas)."
    )

    tabela_display = []
    for g in m_grupos:
        tabela_display.append(
            {
                "Grupo": f"G{g['group']:02d}",
                "Nome do Grupo": g["group_name"],
                "Total": g["total"],
                "No Contexto": g["in_context"],
                "Fora Contexto": g["out_of_context"],
                "Nota Média": f"{g['media_qualidade']:.2f}",
                "Adequadas (%)": f"{g['adequadas_pct']:.1f}%",
                "Fontes Sim": g["fontes_sim"],
                "Fontes Parcial": g["fontes_parcial"],
                "Recusas Seguras": g["recusa_sim"],
            }
        )
    df_tabela = pd.DataFrame(tabela_display)
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

    st.info(
        "💡 **Observação Metodológica**: Para os Grupos 03 e 04 (perguntas deliberadamente fora de contexto), "
        "a expectativa de 'Fontes Corretas' é N/A, pois o comportamento esperado é a recusa segura "
        "sinalizando insuficiência de evidências (100% de sucesso atingido em ambos os grupos)."
    )


# -------------------------------------------------------------
# ABA 3: EXPLORADOR INTERATIVO DAS 60 PERGUNTAS
# -------------------------------------------------------------
with tab_explorador:
    st.subheader("Explorador Detalhado de Perguntas")
    st.markdown("Filtre e inspecione as respostas geradas com e sem RAG e as avaliações manuais.")

    f_col1, f_col2, f_col3, f_col4 = st.columns(4)

    with f_col1:
        grupos_opcoes = ["Todos"] + [f"G{g:02d} — {m_grupos[g-1]['group_name']}" for g in range(1, 11)]
        sel_grupo = st.selectbox("Filtrar por Grupo:", grupos_opcoes)

    with f_col2:
        sel_exp = st.selectbox(
            "Expectativa:",
            ["Todas", "No Contexto (context)", "Fora de Contexto (out_of_context)"],
        )

    with f_col3:
        sel_nota = st.selectbox("Qualidade Geral:", ["Todas", "Nota 5", "Nota 4", "Nota 3", "Nota 2"])

    with f_col4:
        sel_adeq = st.selectbox("Resposta Adequada:", ["Todas", "sim", "parcial", "não"])

    termo_busca = st.text_input("🔍 Busca textual na pergunta ou id (ex: 'pipx', 'JWT', 'G05'):", "").strip()

    # Aplicação dos Filtros
    filtradas = avaliacoes
    if sel_grupo != "Todos":
        g_num = int(sel_grupo[1:3])
        filtradas = [q for q in filtradas if q["group"] == g_num]

    if sel_exp == "No Contexto (context)":
        filtradas = [q for q in filtradas if q["expected"] == "context"]
    elif sel_exp == "Fora de Contexto (out_of_context)":
        filtradas = [q for q in filtradas if q["expected"] == "out_of_context"]

    if sel_nota != "Todas":
        nota_val = int(sel_nota.replace("Nota ", ""))
        filtradas = [q for q in filtradas if q["qualidade"] == nota_val]

    if sel_adeq != "Todas":
        filtradas = [q for q in filtradas if q["resposta_adequada"] == sel_adeq]

    if termo_busca:
        filtradas = [
            q
            for q in filtradas
            if termo_busca.lower() in q["question"].lower()
            or termo_busca.lower() in q["id"].lower()
        ]

    st.markdown(f"**Exibindo {len(filtradas)} de 60 perguntas:**")

    for q in filtradas:
        nota_badge = f"⭐ {q['qualidade']}/5"
        exp_badge = "📘 No Contexto" if q["expected"] == "context" else "🚫 Fora do Contexto"
        status_adeq = q["resposta_adequada"]

        with st.expander(f"[{q['id']}] {q['question']} — ({nota_badge} | {exp_badge} | Adequada: {status_adeq})"):
            m_c1, m_c2, m_c3, m_c4 = st.columns(4)
            m_c1.markdown(f"**Grupo:** G{q['group']:02d} — {q['group_name']}")
            m_c2.markdown(f"**Categorias:** `{' | '.join(q['categories'])}`")
            m_c3.markdown(f"**Fonte Correta:** `{q['fonte_correta']}`")
            m_c4.markdown(f"**Sinalizou Insuficiência:** `{q['sinalizou_insuficiencia']}`")

            st.markdown("---")

            r_col1, r_col2 = st.columns(2)
            with r_col1:
                st.markdown("#### 🤖 Resposta Obtida (Com RAG)")
                st.info(q["resposta_rag"] if q["resposta_rag"] else "*Sem resposta registrada*")
                if q["fontes"]:
                    st.markdown("**Fontes recuperadas pelo retriever:**")
                    for f in q["fontes"]:
                        st.markdown(f"- `{f}`")
                else:
                    st.caption("*Nenhuma fonte recuperada.*")

            with r_col2:
                st.markdown("#### 🧠 Resposta Sem RAG (Modelo Puro)")
                st.warning(q["resposta_sem_rag"] if q["resposta_sem_rag"] else "*Sem resposta registrada*")

            st.markdown("---")
            st.markdown("#### 📝 Análise Qualitativa e Observações")
            st.success(q["observacoes"] if q["observacoes"] else "*Sem observações cadastradas.*")



st.markdown("---")
st.caption("TCC G26 — Sistema RAG Multimodal | Desenvolvido para visualização de resultados acadêmicos.")
