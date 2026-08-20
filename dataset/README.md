# Avaliação da RAG — TCC G26

Conjunto de **60 perguntas** para avaliar o assistente RAG sobre o material do
curso (FastAPI do zero, Introdução ao Python e Python para Processamento de
Dados). A avaliação compara duas condições experimentais: resposta **com RAG**
(contexto recuperado do corpus) e resposta **sem RAG** (pergunta enviada
diretamente ao modelo).

## Arquivos

| Arquivo | Papel |
| --- | --- |
| [`perguntas.json`](perguntas.json) | As 60 perguntas do dataset (10 grupos × 6), com categorias, idioma e expectativa de resposta |
| [`respostas_com_rag.json`](respostas_com_rag.json) | Respostas da condição **com RAG** (via API), incluindo as fontes recuperadas |
| [`respostas_sem_rag.json`](respostas_sem_rag.json) | Respostas da condição **sem RAG** (via Bedrock, sem contexto) |
| [`resultados_avaliacao.md`](resultados_avaliacao.md) | Roteiro de análise consolidado para preencher/avaliar |
| [`consultar_api.py`](consultar_api.py) | Consulta a API RAG e regenera `resultados_avaliacao.md` |
| [`consultar_sem_rag.py`](consultar_sem_rag.py) | Consulta o modelo sem RAG (Bedrock) |
| [`gerar_resultados_base.py`](gerar_resultados_base.py) | Regenera o roteiro com os campos vazios a partir de `perguntas.json` |

## Objetivo

Verificar se o sistema consegue recuperar o conteúdo correto mesmo quando a
pergunta apresenta diferentes níveis de clareza, ruído linguístico e relação
com o material — cobrindo recuperação, robustez e controle de alucinação, e
comparando o resultado com o comportamento do modelo sem RAG.

## Fluxo de trabalho

1. As **respostas com RAG** são obtidas da API do sistema (`consultar_api.py run`,
   com 15 s de intervalo entre requisições) e salvas em `respostas_com_rag.json`.
2. As **respostas sem RAG** são obtidas diretamente do modelo. O script
   `consultar_sem_rag.py run` usa a mesma implementação Bedrock do pipeline
   (mesmos parâmetros) e salva em `respostas_sem_rag.json`.
3. `python dataset/consultar_api.py fill` junta as duas condições em
   `resultados_avaliacao.md`, com a resposta RAG, a resposta sem RAG e as
   fontes recuperadas — ficando os campos de avaliação para preencher.

## Estrutura de `perguntas.json`

O dataset é organizado em **10 grupos** de **6 perguntas cada** (60 no total).
Cada pergunta pode pertencer a **várias categorias** simultaneamente.

| Campo | Descrição |
| --- | --- |
| `id` | Identificador único (`G01-Q01` … `G10-Q06`) |
| `group` | Grupo principal (1–10) |
| `group_name` | Nome do grupo |
| `question` | Texto da pergunta |
| `language` | `pt` ou `en` |
| `categories` | Lista de características (ver tabela abaixo) |
| `expected` | `context` (deve ser respondida pelo corpus) ou `out_of_context` (deve sinalizar evidência insuficiente) |
| `notes` | Observação sobre o que a pergunta avalia |

## Grupos

| Grupo | Nome | O que avalia | Exemplo |
| --- | --- | --- | --- |
| 1 | Perguntas diretas | Recuperação objetiva de informação | "O que é o pipx e para que serve?" |
| 2 | Longas e contextualizadas | Entendimento de contexto e localização da informação | "Na aula sobre autenticação, o professor explica o funcionamento do JWT. Considerando isso, descreva o que são as claims..." |
| 3 | Longas sem relação com o material | Reconhecimento de que a informação não está na base | "Considerando a evolução dos processadores e a Lei de Moore..." |
| 4 | Diretas sem relação com o material | Controle de alucinação | "Quem descobriu o Brasil?" |
| 5 | Erros de ortografia | Robustez a erros ortográficos (pt e en) | "oq é rag e como ele funciona?" |
| 6 | Erros de pontuação | Robustez a ruído textual | "O que é RAG,,, como funciona???" |
| 7 | Emojis | Robustez a elementos não semânticos | "O que é RAG? 🤖📚" |
| 8 | Afirmações | Interpretação de afirmação como solicitação | "RAG utiliza apenas informações armazenadas no modelo." |
| 9 | Gírias | Compreensão de linguagem informal | "Me explica aí, de boa, como esse RAG funciona?" |
| 10 | Sarcasmo/ironia | Compreensão de intenção e resistência a formulações adversas | "Então quer dizer que RAG magicamente sabe tudo, né? 🙄" |

## Categorias

Uma pergunta pode estar em mais de uma categoria:

| Categoria | Descrição | Quantidade |
| --- | --- | --- |
| `direta` | Pergunta curta e objetiva | 12 |
| `curta` | Poucas palavras | 48 |
| `longa` | Frase estendida com contexto | 12 |
| `ingles` | Pergunta em inglês | 8 |
| `erro_ortografia_pt` | Erros de ortografia em português | 4 |
| `erro_ortografia_en` | Erros de ortografia em inglês | 2 |
| `fora_de_contexto` | Tema ausente do corpus | 22 |
| `emoji` | Contém emojis | 8 |
| `giria` | Linguagem informal/gírias | 6 |
| `sem_pontuacao` | Pontuação ausente ou excessiva | 12 |
| `afirmacao` | Enunciada como afirmação | 6 |
| `sarcasmo` | Ironia/sarcasmo | 6 |
| `correta` | Ortografia e pontuação corretas | 12 |
| `contexto` | Conteúdo presente no corpus | 38 |

## Distribuição de expectativa

- `expected: "context"` — **38 perguntas** (deve responder com base no corpus)
- `expected: "out_of_context"` — **22 perguntas** (deve sinalizar evidência insuficiente em vez de inventar)

## Como usar

```python
import json

with open("dataset/perguntas.json", encoding="utf-8") as f:
    dataset = json.load(f)

for q in dataset["questions"]:
    print(q["id"], q["question"])
```

Para avaliação manual: envie cada pergunta ao chat, registre a resposta e as
fontes recuperadas, e confira se:

1. **Respostas corretas** (`expected: context`) trouxeram as fontes certas;
2. **Perguntas fora de contexto** foram sinalizadas como evidência insuficiente
   (sem alucinação);
3. O ruído linguístico (erros, emojis, gírias, sarcasmo) não impediu a recuperação.

## Roteiro de resultados

O arquivo `resultados_avaliacao.md` é o **roteiro de análise** do TCC: uma
seção por pergunta (mesmo id e ordem do JSON), agrupada por grupo, com as
respostas com/sem RAG e as fontes recuperadas já preenchidas automaticamente,
e os campos de avaliação abertos para análise.

Para (re)gerar o roteiro a partir das respostas já coletadas:

```bash
python dataset/consultar_api.py fill
```

Para gerar o roteiro com os campos vazios (sem respostas):

```bash
python dataset/gerar_resultados_base.py
```

### Campos de análise

| Campo | O que preencher |
| --- | --- |
| `Análises` | Análise qualitativa da resposta (aderência, raciocínio, erro observado) |
| `Resposta obtida (RAG)` | Texto da resposta com RAG (preenchido automaticamente) |
| `Resposta sem RAG` | Texto da resposta sem RAG (preenchido automaticamente) |
| `Fontes obtidas` | Fontes recuperadas (arquivo + página/seção/tempo) |
| `Fonte correta recuperada` | `sim` / `nao` / `parcial` — a fonte certa apareceu? |
| `Resposta adequada` | `sim` / `nao` / `parcial` — a resposta responde a pergunta? |
| `Sinalizou insuficiência` | `sim` / `nao` / `n/a` — sinalizou evidência insuficiente (esperado nas 22 fora de contexto) |
| `Qualidade geral (1–5)` | Nota 1–5 (relevância, fidelidade ao material, clareza) |
| `Observações` | Notas livres (ex.: ruído que atrapalhou, fonte errada recuperada) |

### Leitura dos resultados para o TCC

- **Fidelidade**: `resposta_adequada = sim` + `fonte_correta_recuperada = sim`
  indicam resposta sustentada pelo material (princípio do RAG).
- **Controle de alucinação**: nas 22 perguntas `out_of_context`,
  `sinalizou_insuficiencia = sim` é o comportamento correto — qualquer resposta
  inventada deve ser marcada como `nao` e discutida no trabalho.
- **Robustez linguística**: compare `fonte_correta_recuperada` entre as
  perguntas limpas e as com ruído (erros, emojis, gírias) para medir a queda
  de qualidade da recuperação.
- **Comparação com/sem RAG**: contraste a `resposta adequada` entre
  `respostas_com_rag.json` e `respostas_sem_rag.json` para evidenciar o ganho
  da recuperação e o comportamento de alucinação sem contexto.
- **Relatório**: a distribuição das notas `qualidade_geral` por grupo alimenta
  a análise de cada cenário no capítulo de avaliação.