# tcc_rag_g26

**⚠️ Nota de Licenciamento:** O código-fonte original deste projeto está sob a licença GPLv3 (arquivo `LICENSE`). No entanto, todos os textos, anotações, apostilas e materiais didáticos baseados no curso de Eduardo Mendes (@dunossauro) contidos na pasta `content/` seguem estritamente a licença Creative Commons BY-NC-SA 4.0 (ver `content/README.md` e `content/LICENSE-CONTENT`).

# arquitetura-rag.md

# Arquitetura da RAG Multimodal

## 1. Objetivo

Este documento descreve a arquitetura da aplicação de Retrieval-Augmented Generation (RAG) desenvolvida para o projeto.

O sistema tem como objetivo permitir que estudantes realizem perguntas em linguagem natural sobre conteúdos provenientes de materiais educacionais em diferentes formatos:

- PDF (apostilas, slides, exercícios, ementas e outros documentos autorizados);
- Markdown;
- Vídeo (videoaulas, com transcrição do áudio).

Os arquivos são processados, transformados em unidades textuais (*chunks*), convertidos em embeddings e armazenados em um banco PostgreSQL com extensão pgvector.

Durante uma consulta, a pergunta do usuário também é transformada em embedding. O sistema realiza uma busca vetorial, recupera os conteúdos mais relevantes e envia o contexto selecionado juntamente com a pergunta para um Large Language Model (LLM), responsável pela geração da resposta. A resposta é apresentada junto com a indicação dos documentos e páginas (ou trechos) utilizados como fonte.

Quando a evidência recuperada for insuficiente para responder à pergunta, o sistema deverá sinalizar essa limitação, em vez de completar a resposta com informações não presentes nos materiais.

---

## 2. Arquitetura geral

```text
                    ┌──────────────────────────────┐
                    │          Streamlit           │
                    │           Frontend           │
                    │       Upload + Chat          │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │            FastAPI            │
                    │            Backend            │
                    └──────────────┬───────────────┘
                                   │
               ┌───────────────────┴───────────────────┐
               │                                       │
               ▼                                       ▼
     ┌──────────────────────┐               ┌──────────────────────┐
     │       INGESTÃO       │               │       CONSULTA       │
     │                      │               │                      │
     │ Conversão dos        │               │ Pergunta do usuário  │
     │ arquivos brutos em   │               │ em consulta vetorial │
     │ conteúdo estruturado │               └──────────┬───────────┘
     │ para a RAG           │                          │
     └──────────┬───────────┘                          ▼
                │                             Titan Embeddings
                ▼                              (AWS Bedrock)
        ┌───────────────┐                               │
        │   Amazon S3   │                               ▼
        │               │                        PostgreSQL
        │ Arquivos      │                        + pgvector
        │ originais     │                               │
        └───────┬───────┘                               ▼
                │                                 Top-K Chunks
       ┌────────┼─────────┐                           │
       ▼        ▼         ▼                           ▼
    Docling  Python    FFmpeg                 Contexto + Pergunta
       │        │         │                           │
       │        │         ▼                           ▼
       │        │  Amazon                            DeepSeek
       │        │  Transcribe                       (AWS Bedrock)
       │        │         │                           │
       └────────┴─────────┘                           ▼
                │                                  Resposta
                ▼                                  + Fontes
           Chunking
          (LangChain)
                │
                ▼
        Titan Embeddings
         (AWS Bedrock)
                │
                ▼
        PostgreSQL
        + pgvector
```

## 3. Componentes

| Componente | Tecnologia | Responsabilidade |
| --- | --- | --- |
| Frontend | Streamlit | Interface de upload e chatbot |
| Backend | FastAPI | API e lógica da aplicação |
| Armazenamento | Amazon S3 | Armazenamento dos arquivos originais |
| Banco de dados | PostgreSQL | Dados estruturados e metadados |
| Vector Store | pgvector | Armazenamento e busca dos embeddings |
| PDF | Docling | Extração e estruturação de documentos PDF |
| Markdown | Python | Leitura e processamento de arquivos Markdown |
| Vídeo | FFmpeg | Extração do áudio dos vídeos |
| Transcrição | Amazon Transcribe | Conversão de áudio em texto |
| Chunking | LangChain | Fragmentação dos documentos |
| Embeddings | Amazon Titan Text Embeddings V2 / AWS Bedrock | Conversão do conteúdo em vetores |
| Retrieval | pgvector | Busca dos chunks semanticamente semelhantes |
| LLM | DeepSeek / AWS Bedrock | Geração das respostas |
| Orquestração | LangChain | Integração das etapas da RAG |
| Containerização | Docker | Padronização do ambiente |

## 4. Fluxo de ingestão

A ingestão é responsável por transformar os arquivos enviados pelo usuário em informações que possam ser recuperadas pela RAG.

```text
Arquivo
   │
   ▼
FastAPI
   │
   ├──────────────────────► Amazon S3
   │                         Arquivo original
   │
   ▼
Processamento
   │
   ├── PDF
   │    └── Docling
   │
   ├── Markdown
   │    └── Python
   │
   └── Vídeo
        └── FFmpeg
             └── Amazon Transcribe
   │
   ▼
Conteúdo textual estruturado
   │
   ▼
Chunking
(LangChain)
   │
   ▼
Embeddings
(Titan / AWS Bedrock)
   │
   ▼
PostgreSQL + pgvector
```

## 5. Armazenamento dos arquivos

Os arquivos originais enviados pelos usuários serão armazenados no Amazon S3.

O S3 terá a responsabilidade de preservar os arquivos originais independentemente do processamento realizado pela RAG.

Adicionalmente, os materiais do curso serão versionados no repositório, na pasta `content/`, sob a licença CC BY-NC-SA (ver `content/README.md` e `content/LICENSE-CONTENT`).

Exemplo:

```text
s3://rag-tcc/
│
├── documents/
│   ├── apostila-machine-learning.pdf
│   └── aula-01.md
│
└── audio/
    ├── aula-01.mp3
    └── aula-02.mp3
```

Correspondência no repositório:

```text
content/
├── documents/   # PDFs (apostilas, slides, exercícios, ementas)
├── markdown/    # documentação em Markdown
└── audio/       # áudios extraídos das videoaulas
```

O banco PostgreSQL não precisa armazenar o arquivo binário.

Ele armazenará os metadados necessários para relacionar os chunks ao arquivo original, incluindo a página (PDF), a seção (Markdown) ou o trecho temporizado (áudio/vídeo) de origem, permitindo indicar as fontes nas respostas.

## 6. Processamento de PDF

Os arquivos PDF serão processados utilizando o Docling.

Fluxo:

```text
PDF
 │
 ▼
Docling
 │
 ▼
Texto estruturado
 │
 ▼
Metadados
 │
 ▼
Chunking
```

Quando possível, informações como páginas, títulos e estrutura do documento serão preservadas como metadados.

Esses metadados são essenciais para cumprir o requisito de indicar os documentos e as páginas que fundamentam cada resposta.

## 7. Processamento de Markdown

Arquivos Markdown serão processados utilizando Python e as ferramentas de parsing disponíveis.

A estrutura hierárquica do Markdown poderá ser utilizada para preservar o contexto:

```markdown
# Machine Learning

## Supervised Learning

Conteúdo...

### Classification

Conteúdo...
```

O contexto hierárquico será preservado durante a criação dos chunks.

## 8. Processamento de vídeo

Os vídeos serão processados em duas etapas: extração do áudio e transcrição.

```text
Vídeo
  │
  ▼
FFmpeg
  │
  ▼
Áudio
  │
  ▼
Amazon Transcribe
  │
  ▼
Transcrição
  │
  ▼
Chunking
```

A transcrição será tratada como conteúdo textual e posteriormente incorporada ao pipeline de embeddings.

Os metadados do vídeo (arquivo de origem e marcações temporais da transcrição) deverão ser preservados para permitir a identificação da origem da informação.

## 9. Chunking

O conteúdo processado será dividido em unidades menores denominadas chunks.

O objetivo é evitar que documentos inteiros sejam transformados em um único embedding.

```text
Documento
    │
    ▼
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
Chunk N
```

A estratégia de chunking adotada será fixa em todas as execuções do projeto, priorizando a preservação do contexto semântico por meio de chunking semântico/hierárquico.

Para documentos estruturados, serão utilizadas informações como:

- títulos;
- subtítulos;
- seções;
- parágrafos;
- blocos de código.

Cada chunk carregará os metadados de origem (arquivo e página/seção/tempo).

O LangChain será utilizado para auxiliar nessa etapa.

Como a estratégia de chunking não é objeto de comparação experimental, ela será definida uma única vez e mantida constante em todos os experimentos.

## 10. Geração dos embeddings

Cada chunk será convertido em um vetor utilizando o Amazon Titan Text Embeddings V2 disponibilizado pelo AWS Bedrock.

```text
Chunk
  │
  ▼
Titan Text Embeddings V2
(AWS Bedrock)
  │
  ▼
[0.012, -0.431, 0.827, ...]
```

O mesmo modelo de embedding deverá ser utilizado para:

- gerar embeddings dos documentos;
- gerar embeddings das perguntas.

Isso garante que documentos e consultas estejam no mesmo espaço vetorial.

## 11. PostgreSQL + pgvector

O PostgreSQL será utilizado como banco de dados principal.

A extensão pgvector será utilizada para armazenar e consultar os embeddings.

Estrutura conceitual:

```text
documents
    │
    ├── id
    ├── filename
    ├── type
    ├── s3_key
    └── metadata
         │
         ▼
chunks
    │
    ├── id
    ├── document_id
    ├── content
    ├── metadata (inclui página/seção/tempo de origem)
    └── embedding
```

O relacionamento entre documentos e chunks permite rastrear a origem de cada informação recuperada e indicar as fontes nas respostas.

## 12. Retrieval

Quando o usuário realiza uma pergunta, ela é transformada em embedding.

```text
Pergunta
   │
   ▼
Titan Embeddings
(AWS Bedrock)
   │
   ▼
Vetor da consulta
   │
   ▼
pgvector
   │
   ▼
Busca por similaridade
   │
   ▼
Top-K Chunks
```

O parâmetro K determina quantos chunks serão recuperados.

Exemplo:

```text
K = 3
```

Nesse caso, os 3 chunks mais semelhantes serão recuperados.

O valor de K será definido uma única vez e mantido fixo em todas as execuções do projeto, garantindo que a única variável experimental seja a presença ou ausência da RAG.

## 13. Construção do contexto

Os melhores chunks serão combinados com a pergunta do usuário.

```text
Pergunta
    +
Top-K Chunks
    │
    ▼
Contexto + Pergunta
   (LangChain)
```

O contexto será utilizado para instruir o LLM a responder utilizando somente as informações recuperadas.

## 14. Geração da resposta

O contexto e a pergunta serão enviados ao DeepSeek por meio do AWS Bedrock.

```text
Contexto + Pergunta
        │
        ▼
DeepSeek
(AWS Bedrock)
        │
        ▼
Resposta + Fontes (documento/página/seção/tempo)
```

A resposta deverá ser fundamentada nas informações recuperadas pela RAG.

As instruções fornecidas ao LLM (prompt) deverão determinar que, quando a evidência recuperada for insuficiente, o sistema sinalize essa limitação em vez de gerar informações não presentes nos materiais.

## 15. Fluxo completo de consulta

```text
Usuário
   │
   ▼
Streamlit
   │
   ▼
FastAPI
   │
   ▼
Titan Embeddings
(AWS Bedrock)
   │
   ▼
PostgreSQL + pgvector
   │
   ▼
Top-K
   │
   ▼
Contexto + Pergunta
(LangChain)
   │
   ▼
DeepSeek
(AWS Bedrock)
   │
   ▼
Resposta + Fontes
   │
   ▼
Streamlit
```

## 16. Estrutura sugerida do projeto

```text
rag-tcc/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── main.py
│   │
│   ├── ingestion/
│   │   ├── pdf.py
│   │   ├── markdown.py
│   │   ├── video.py
│   │   └── chunking.py
│   │
│   ├── embeddings/
│   │   └── bedrock.py
│   │
│   ├── retrieval/
│   │   └── vector_search.py
│   │
│   ├── llm/
│   │   └── bedrock.py
│   │
│   ├── storage/
│   │   └── s3.py
│   │
│   ├── database/
│   │   ├── models.py
│   │   └── connection.py
│   │
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── evaluation/
│   ├── datasets/
│   │   └── questions.json
│   ├── results/
│   ├── run_eval.py
│   ├── metrics.py
│   └── README.md
│
├── docker/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 17. Containerização

O Docker será utilizado para garantir um ambiente reprodutível.

A aplicação poderá ser executada com:

```bash
docker compose up
```

A infraestrutura mínima local será composta por:

```text
Docker Compose
│
├── FastAPI
│
├── Streamlit
│
└── PostgreSQL + pgvector
```

Os serviços externos serão acessados por API:

- AWS Bedrock
- Amazon S3
- Amazon Transcribe

## 18. Escopo

O sistema terá como funcionalidades principais:

- upload de PDF;
- upload de Markdown;
- upload de vídeo;
- armazenamento dos arquivos no S3;
- processamento dos documentos;
- transcrição de vídeos;
- chunking;
- geração de embeddings;
- armazenamento vetorial;
- recuperação por similaridade;
- geração de respostas utilizando LLM;
- indicação dos documentos e trechos que fundamentam cada resposta;
- sinalização quando a evidência recuperada for insuficiente;
- apresentação das respostas no Streamlit;
- avaliação comparando LLM puro e LLM+RAG com métricas quantitativas e análise manual dos integrantes.

Não fazem parte do escopo inicial:

- reranking;
- RAGAS;
- Kubernetes;
- microsserviços;
- Kafka;
- Redis;
- WebSockets;
- agentes autônomos;
- fine-tuning de LLM;
- treinamento de modelos próprios;
- memória conversacional avançada;
- medição de aprendizagem ou desempenho acadêmico dos estudantes.

## 19. Stack final

```text
Frontend
└── Streamlit


Backend
└── FastAPI


Storage
└── Amazon S3


Database
└── PostgreSQL + pgvector


Document Processing
├── Docling
├── Python
└── FFmpeg


Video Transcription
└── Amazon Transcribe


Embeddings
└── Amazon Titan Text Embeddings V2 / AWS Bedrock


RAG
└── LangChain


Retrieval
└── pgvector


LLM
└── DeepSeek / AWS Bedrock


Infrastructure
└── Docker
```

---

# avaliacao-rag.md

# Avaliação da RAG

## 1. Objetivo

O objetivo desta etapa é avaliar o desempenho do sistema de Retrieval-Augmented Generation (RAG) em comparação com o LLM puro, verificando a hipótese do trabalho:

> A incorporação de uma etapa de recuperação de informações de materiais educacionais ao fluxo de um modelo de linguagem produzirá, para um mesmo conjunto de perguntas, respostas mais factuais, relevantes e contextualizadas, além de reduzir a ocorrência de informações não sustentadas pelos documentos, quando comparada ao uso do modelo de linguagem sem recuperação externa.

**A avaliação será realizada pelos três integrantes do grupo**, por meio da classificação manual das respostas (correta, parcialmente correta ou incorreta), complementada por métricas quantitativas automáticas da recuperação.

A avaliação será executada exclusivamente durante a etapa experimental do projeto, separada do fluxo normal de atendimento das perguntas dos usuários.

## 2. Separação entre aplicação e avaliação

### Aplicação

```text
Pergunta
   │
   ▼
Embedding
   │
   ▼
pgvector
   │
   ▼
Top-K
   │
   ▼
Contexto
   │
   ▼
DeepSeek
   │
   ▼
Resposta + Fontes
```

### Avaliação

```text
Dataset de perguntas
        │
        ▼
  LLM puro ──┐
             ├──► Respostas
  LLM+RAG ───┘
             │
             ▼
  Métricas automáticas da recuperação (LLM+RAG)
  Classificação manual pelos 3 integrantes
             │
             ▼
         Resultados
```

## 3. Dataset de avaliação

Será criado um conjunto de perguntas representativas dos documentos utilizados na base de conhecimento, elaborado pelos integrantes do grupo.

Importante: os materiais do curso (PDFs, transcrições das aulas, documentações em Markdown) são previamente ingeridos e indexados no pgvector. O dataset de avaliação é um artefato interno do experimento — o usuário da aplicação apenas faz perguntas e nunca fornece arquivos ou referências.

Para cada pergunta do dataset, os integrantes anotarão onde a resposta se encontra no corpus já indexado. Essa anotação funciona como gabarito, permitindo verificar automaticamente se o sistema recuperou os trechos corretos.

Cada pergunta deverá possuir:

- pergunta;
- resposta de referência (`ground_truth`);
- trechos relevantes previamente identificados (chunks do corpus já indexado, com página/seção/tempo para localização humana).

Exemplo:

```json
{
  "id": 1,
  "question": "O que é overfitting?",
  "ground_truth": "Overfitting ocorre quando um modelo aprende excessivamente os padrões dos dados de treinamento.",
  "relevant_chunks": ["apostila-machine-learning.pdf:pagina 42"],
  "relevant_pages": [42]
}
```

O dataset deverá conter perguntas relacionadas aos diferentes tipos de conteúdo utilizados na aplicação (PDF, Markdown e vídeo).

O dataset será congelado antes do início dos experimentos e versionado no repositório, garantindo que as duas condições experimentais sejam avaliadas com exatamente o mesmo conjunto de perguntas.

## 4. Experimentos

### Experimento 1 — LLM puro

```text
Pergunta
    ↓
DeepSeek
    ↓
Resposta
```

Objetivo:

Estabelecer o desempenho do LLM sem acesso ao contexto recuperado, respondendo apenas com seu conhecimento paramétrico.

### Experimento 2 — LLM+RAG

```text
Pergunta
    ↓
Titan Embeddings
    ↓
pgvector
    ↓
Top-K
    ↓
DeepSeek
    ↓
Resposta + Fontes
```

Objetivo:

Avaliar se o acesso ao contexto recuperado dos documentos melhora a correção e a relevância das respostas em comparação ao LLM puro.

As duas condições utilizam exatamente o mesmo dataset de perguntas e o mesmo modelo generativo (DeepSeek), isolando a RAG como única variável experimental.

## 5. Avaliação pelos três integrantes

**Esta é a etapa central da avaliação.**

Cada um dos três integrantes do grupo classificará, de forma independente, todas as respostas produzidas nas duas condições (LLM puro e LLM+RAG), com base na pergunta, na resposta de referência e no conteúdo dos documentos.

Cada resposta será classificada como:

- correta;
- parcialmente correta;
- incorreta.

Critérios:

- a resposta está correta em relação à resposta de referência e ao conteúdo dos documentos?
- a resposta é pertinente à pergunta realizada?
- a resposta é sustentada pelo corpus (no caso do LLM+RAG, pelos trechos recuperados)?

Cada avaliador registrará sua classificação em uma planilha compartilhada. Divergências entre avaliadores serão discutidas e resolvidas em consenso, com registro da decisão.

Como referência preliminar, será considerado satisfatório obter pelo menos 70% de respostas classificadas como corretas ou parcialmente corretas. Esse valor é apenas um parâmetro de acompanhamento e deverá ser interpretado em função do tamanho, da dificuldade e da composição do corpus.

## 6. Métricas automáticas da recuperação

Aplicáveis apenas à condição com RAG. Calculadas automaticamente por script, comparando os chunks recuperados com os trechos relevantes anotados no dataset.

- **Precision@K**: proporção dos chunks recuperados que são relevantes;
- **Recall@K**: proporção das informações relevantes existentes que foram recuperadas.

## 7. Comparação dos resultados

Os resultados serão apresentados em tabelas e gráficos.

### Classificação manual das respostas (3 avaliadores)

| Classificação | LLM puro | LLM+RAG |
| ------------- | -------- | ------- |
| Correta | XX% | XX% |
| Parcialmente correta | XX% | XX% |
| Incorreta | XX% | XX% |
| Correta + Parcial | XX% | XX% |

### Métricas automáticas da recuperação (apenas LLM+RAG)

| Métrica | Valor |
| ------- | ----- |
| Precision@K | 0.XX |
| Recall@K | 0.XX |

Os principais erros encontrados (falhas na extração, transcrição, recuperação de trechos irrelevantes, geração de informações não presentes no corpus) serão documentados, orientando ajustes e recomendações para outros acervos educacionais.

## 8. Estrutura do código de avaliação

```text
evaluation/
│
├── datasets/
│   └── questions.json
│
├── results/
│   ├── llm_pure.json
│   ├── llm_rag.json
│   └── retrieval_metrics.json
│
├── run_eval.py
├── metrics.py
└── README.md
```

- `run_eval.py`: executa o dataset de perguntas nas duas condições e salva as respostas (e os contextos recuperados) em `results/`;
- `metrics.py`: calcula Precision@K e Recall@K a partir dos contextos recuperados e dos trechos relevantes anotados;
- a planilha de classificação manual é preenchida pelos três avaliadores a partir das respostas salvas em `results/`.

## 9. Execução

A avaliação poderá ser executada separadamente da aplicação:

```bash
python evaluation/run_eval.py
python evaluation/metrics.py
```

Fluxo:

```text
questions.json
      │
      ▼
LLM puro ──┐
           ├──► Respostas (results/)
LLM+RAG ───┘
           │
           ▼
Contextos recuperados (LLM+RAG)
           │
           ▼
metrics.py ──► retrieval_metrics.json
           │
           ▼
Planilha de classificação manual (3 avaliadores)
           │
           ▼
Comparação dos resultados
```

## 10. Princípios metodológicos

- o dataset de perguntas será congelado antes do início dos experimentos;
- o modelo generativo será o mesmo nas duas condições (DeepSeek);
- o valor de K do Top-K será o mesmo em todas as execuções;
- a estratégia de chunking será mantida constante;
- os três avaliadores classificarão as respostas de forma independente antes da reunião de consenso.

Isso permite uma comparação controlada, isolando a presença da RAG como única variável experimental.
