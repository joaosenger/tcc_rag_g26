# tcc_rag_g26

**⚠️ Nota de Licenciamento:** O código-fonte original deste projeto está sob a licença GPLv3 (arquivo `LICENSE`). No entanto, todos os textos, anotações, apostilas e materiais didáticos baseados no curso de Eduardo Mendes (@dunossauro) contidos na pasta `content/` seguem estritamente a licença Creative Commons BY-NC-SA 4.0 (ver `content/README.md` e `content/LICENSE-CONTENT`).

---

## Início rápido

### Pré-requisitos

- Python 3.12+
- Docker e Docker Compose
- FFmpeg (para transcrição de áudio com Whisper)
- Credenciais AWS com acesso ao Bedrock (Titan Embeddings + DeepSeek)

### 1. Configurar variáveis de ambiente

```bash
cp .example.env .env
# Edite .env e preencha com suas credenciais AWS
```

Variáveis necessárias (ver `.example.env`):

| Variável | Descrição |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | Chave de acesso AWS (IAM) |
| `AWS_SECRET_ACCESS_KEY` | Chave secreta AWS |
| `AWS_REGION` | Região AWS (ex.: `us-east-1`) |
| `BEDROCK_EMBEDDING_MODEL` | Modelo de embedding (`amazon.titan-embed-text-v2:0`) |
| `BEDROCK_LLM_MODEL` | Modelo LLM (`us.deepseek.r1-v1:0`) |
| `POSTGRES_USER` | Usuário do banco (padrão: `rag`) |
| `POSTGRES_PASSWORD` | Senha do banco (padrão: `rag`) |
| `POSTGRES_DB` | Nome do banco (padrão: `rag`) |
| `POSTGRES_HOST` | Host do banco (`localhost` local, `postgres` no compose) |
| `POSTGRES_PORT` | Porta do banco (padrão: `5432`) |
| `API_URL` | URL da API para o frontend (`http://localhost:8000`) |

> As credenciais AWS podem ficar vazias no `.env` se você usar o perfil default em `~/.aws/credentials` — o boto3 assume automaticamente.

### 2. Configurar credenciais do frontend (login)

```bash
cp .streamlit/secrets.example.toml .streamlit/secrets.toml
# Edite .streamlit/secrets.toml e defina usuário e senha do acesso
```

O frontend Streamlit exige login antes de mostrar o chat.

### 3. Instalar dependências

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

### 4. Subir o banco de dados

```bash
docker compose up -d postgres
```

### 5. Criar as tabelas

```bash
python -m app.database.init_db
```

### 6. Obter os materiais do curso

> Os PDFs e Markdowns das aulas **estão versionados no repositório** (licença CC BY-NC-SA, ver `content/documents/LICENSE-CONTENT`). Os **MP3s das videoaulas não estão** (por tamanho, licença CC BY-NC-SA) — obtenha-os das videoaulas do curso e coloque-os em `content/audio/`:
>
> - **PDFs** → `content/documents/` (apostilas, slides, exercícios)
> - **Markdown** → `content/markdown/aulas/` (já versionado no repo)
> - **Áudios MP3** → `content/audio/` (obter das videoaulas do curso)

### 7. Transcrever áudios (uma vez só)

Requer GPU (recomendado) ou CPU com pelo menos 4 GB RAM.

```bash
# Transcrever todas as aulas de uma vez
python content/audio/transcribe_all.py --batch-size 32

# Ou transcrever uma aula específica
python content/audio/audio_transcript.py content/audio/aula-00.mp3
```

As transcrições são salvas em `content/audio/transcriptions/` (`.md` + `.json`).

### 8. Subir a API (ela ingere o corpus automaticamente)

```bash
uvicorn app.main:app --reload
```

Na primeira inicialização, se o banco estiver vazio, a API **ingere automaticamente** todos os materiais de `content/` (markdowns, PDFs e transcrições de áudio). Isso acontece só uma vez — nas próximas inicializações o banco já está populado.

A API fica disponível em `http://localhost:8000` (documentação em `/docs`).

### 9. Subir o frontend (Streamlit)

Em outro terminal:

```bash
streamlit run frontend/app.py
```

Abra `http://localhost:8501` no navegador e faça login (credenciais definidas no passo 2).

### 10. Fazer perguntas

1. Digite sua pergunta no campo de chat e pressione **Enter**
2. A resposta aparece com:
   - **Texto da resposta** (gerada pelo DeepSeek com base no contexto recuperado)
   - **Fontes** (clique em "Fontes" para expandir — mostra arquivo, página/seção/tempo, score e trecho)
   - **Aviso amarelo** se a evidência for insuficiente

Exemplos de perguntas:
- "Qual o editor que o professor usa durante o curso?"
- "O que significa LAN?"
- "Quais os tipos de dados em Python?"
- "O que é o pipx e para que serve?"

### Tudo via Docker Compose

```bash
docker compose up
```

Isso sobe FastAPI (porta 8000), Streamlit (porta 8501) e PostgreSQL (porta 5432). A auto-ingestão roda na primeira inicialização do FastAPI.

> ⚠️ **Nota:** a imagem Docker **não inclui os MP3s** do corpus (excluídos no `.dockerignore` por tamanho). Dentro do container são ingeridos os PDFs, Markdowns e as transcrições. **Para a apresentação, recomendamos o fluxo local** (passos 8 e 9), que usa o corpus completo já presente em `content/`.

### Rodar os testes

```bash
pytest
```

### Estrutura do projeto

```text
tcc_rag_g26/
├── app/
│   ├── api/routes/          # endpoints FastAPI (documents, chat, health)
│   ├── config/              # configurações centralizadas (chunking, settings)
│   ├── database/            # modelos, conexão, CRUD, init_db
│   ├── embeddings/          # Amazon Titan (Bedrock)
│   ├── ingestion/           # PDF, Markdown, chunking, pipeline, auto_ingest
│   ├── llm/                 # DeepSeek (Bedrock), prompt
│   └── retrieval/           # busca vetorial Top-K
├── content/
│   ├── audio/               # MP3s + transcrições
│   │   ├── transcriptions/  # .md + .json gerados pelo Whisper
│   │   ├── audio_transcript.py
│   │   └── transcribe_all.py
│   ├── documents/           # PDFs do curso (CC BY-NC-SA)
│   └── markdown/aulas/      # Markdown das aulas
├── frontend/
│   ├── app.py               # Streamlit (login + chat)
│   ├── auth.py              # validação de credenciais (login)
│   └── utils.py             # funções puras
├── scripts/
│   └── ingest_corpus.py     # ingestão manual via API (opcional)
├── tests/                   # pytest (unitários)
├── docker/
│   ├── entrypoint.sh        # init_db + uvicorn
│   └── postgres/init/       # CREATE EXTENSION vector
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── requirements-dev.txt
```

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
                    │       Chat (perguntas)      │
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
         │   content/    │                               ▼
         │   (local)     │                        PostgreSQL
         │               │                        + pgvector
         │ Arquivos      │                               │
         │ originais     │                               ▼
         └───────┬───────┘                         Top-K Chunks
       ┌────────┼─────────┐                           │
       ▼        ▼         ▼                           ▼
    Docling  Python   Áudio mp3              Contexto + Pergunta
       │        │         │                           │
       │        │         ▼                           ▼
       │        │  Whisper                           DeepSeek
       │        │  (local)                           (AWS Bedrock)
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
| Frontend | Streamlit | Interface de chat (perguntas) |
| Backend | FastAPI | API e lógica da aplicação |
| Armazenamento | Local (`content/`) | Arquivos originais mantidos localmente |
| Banco de dados | PostgreSQL | Dados estruturados e metadados |
| Vector Store | pgvector | Armazenamento e busca dos embeddings |
| PDF | Docling | Extração e estruturação de documentos PDF |
| Markdown | Python | Leitura e processamento de arquivos Markdown |
| Áudio | Whisper / FFmpeg | Transcrição local dos áudios das aulas |
| Transcrição | Whisper (local) | Conversão de áudio em texto |
| Chunking | LangChain (text splitters) | Fragmentação dos documentos |
| Embeddings | Amazon Titan Text Embeddings V2 / AWS Bedrock | Conversão do conteúdo em vetores |
| Retrieval | pgvector | Busca dos chunks semanticamente semelhantes |
| LLM | DeepSeek-R1 / AWS Bedrock | Geração das respostas |
| Containerização | Docker | Padronização do ambiente |

## 4. Fluxo de ingestão

A ingestão é responsável por transformar os arquivos enviados pelo usuário em informações que possam ser recuperadas pela RAG.

```text
Arquivo
   │
   ▼
FastAPI
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
        └── Áudio (.mp3)
             └── Whisper (local)
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

Os arquivos originais enviados pelos usuários são mantidos localmente na pasta `content/`.

Adicionalmente, os materiais do curso serão versionados no repositório, na pasta `content/`, sob a licença CC BY-NC-SA (ver `content/README.md` e `content/LICENSE-CONTENT`).

Exemplo:

```text
content/
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

## 8. Processamento de áudio

Os áudios das aulas (`.mp3` em `content/audio/`, obtidos manualmente) são transcritos localmente com o Whisper (`faster-whisper` sobre `openai-whisper`, modelo `small`, pt-BR, com aceleração por GPU quando disponível).

```text
Áudio (.mp3)
  │
  ▼
Whisper (local, modelo small)
  │
  ▼
Transcrição (.md + .json) em content/audio/transcriptions/
  │
  ▼
Chunking
```

A transcrição será tratada como conteúdo textual e posteriormente incorporada ao pipeline de embeddings.

Os metadados do vídeo (arquivo de origem e marcações temporais da transcrição) deverão ser preservados para permitir a identificação da origem da informação.

## 9. Chunking

O conteúdo processado é dividido em unidades menores denominadas chunks.

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

A estratégia de chunking é fixa e centralizada em `app/config/chunking.py`:

```python
CHUNK_SIZE = 1024          # caracteres
CHUNK_OVERLAP = 128        # caracteres (~12,5%)
TOP_K = 5                  # chunks recuperados por pergunta
SEPARATORS = ["\n\n", "\n", ". ", " ", ""]
```

Para cada tipo de conteúdo:

- **PDF**: `RecursiveCharacterTextSplitter` sobre os blocos extraídos pelo Docling, mantendo `page` e `heading`.
- **Markdown**: `RecursiveCharacterTextSplitter` sobre os blocos extraídos pelo parser interno, mantendo `section` e `title`.
- **Áudio**: agrupamento de segmentos Whisper consecutivos até atingir `CHUNK_SIZE`, mantendo `start` e `end` no formato `HH:MM:SS`.

Cada chunk carrega os metadados de origem (arquivo e página/seção/tempo).

O LangChain (`langchain-text-splitters`) é utilizado para auxiliar nessa etapa.

Como a estratégia de chunking não é objeto de comparação experimental, ela foi definida uma única vez e mantida constante em todos os experimentos.

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

O valor de K é fixo e definido em `app/config/chunking.py`:

```text
K = 5
```

Nesse caso, os 5 chunks mais semelhantes serão recuperados.

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
   (app/llm/prompt.py)
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

## 16. API (endpoints)

| Método | Rota | Função |
| --- | --- | --- |
| POST | `/api/documents` | Ingestão de um arquivo do corpus (multipart) |
| GET | `/api/documents` | Lista documentos ingeridos |
| POST | `/api/chat` | Recebe pergunta, retorna resposta + fontes |
| GET | `/health` | Healthcheck |

## 17. Estrutura do projeto

```text
tcc_rag_g26/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── chat.py             # POST /api/chat (RAG)
│   │   │   └── documents.py        # POST/GET /api/documents
│   │   └── main.py                 # App FastAPI + healthcheck
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py             # configurações gerais (AWS, Bedrock)
│   │   └── chunking.py             # constantes de chunking (congeladas)
│   │
│   ├── database/
│   │   ├── connection.py           # engine SQLAlchemy + SessionLocal
│   │   ├── crud.py                 # CRUD + similarity_search
│   │   ├── init_db.py              # cria tabelas + extensão vector
│   │   └── models.py               # modelos Document e Chunk
│   │
│   ├── embeddings/
│   │   └── bedrock.py              # Amazon Titan V2 (1024 dims)
│   │
│   ├── ingestion/
│   │   ├── chunking.py             # splitters (PDF, Markdown, áudio)
│   │   ├── markdown.py             # extração com hierarquia de seções
│   │   ├── pdf.py                  # extração com Docling (fast mode)
│   │   ├── pipeline.py             # orquestra: extrair → chunkar → embeddar → persistir
│   │   └── video.py                # transcrição com Whisper (legado)
│   │
│   ├── llm/
│   │   ├── bedrock.py              # DeepSeek-R1 via Converse API + retry
│   │   └── prompt.py               # build_prompt + format_sources
│   │
│   ├── retrieval/
│   │   └── vector_search.py        # retrieve_top_k (K fixo da config)
│   │
│   └── main.py                     # ponto de entrada (expõe app)
│
├── content/
│   ├── audio/
│   │   ├── transcriptions/         # .md + .json gerados pelo Whisper
│   │   ├── audio_transcript.py     # transcrição individual
│   │   ├── transcribe_all.py       # transcrição em lote
│   │   └── aula-NN.mp3             # áudios originais (fora do git)
│   ├── documents/                  # PDFs do curso (CC BY-NC-SA)
│   └── markdown/aulas/             # Markdown das aulas
│
├── frontend/
│   ├── __init__.py
│   ├── app.py                      # Streamlit (login + chat + sidebar)
│   ├── auth.py                     # validação de credenciais
│   └── utils.py                    # funções puras (format_source, PDFs, is_insufficient)
│
├── tests/                          # pytest (testes unitários)
│   └── test_unit_*.py              # testes unitários (sem AWS/banco)
│
├── docker/
│   └── postgres/init/              # CREATE EXTENSION vector
│
├── Dockerfile
├── docker-compose.yml              # FastAPI + Streamlit + PostgreSQL
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## 18. Containerização

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

- AWS Bedrock (embeddings + LLM)

## 19. Escopo

O sistema terá como funcionalidades principais:

- ingestão de PDF;
- ingestão de Markdown;
- ingestão de áudio (videoaulas);
- processamento e armazenamento local dos arquivos (corpus em `content/`);
- processamento dos documentos;
- transcrição de áudios;
- chunking;
- geração de embeddings;
- armazenamento vetorial;
- recuperação por similaridade;
- geração de respostas utilizando LLM;
- indicação dos documentos e trechos que fundamentam cada resposta;
- sinalização quando a evidência recuperada for insuficiente;
- apresentação das respostas no Streamlit.

Não fazem parte do escopo inicial:

- upload de arquivos pelo usuário (corpus gerenciado localmente);
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
- avaliação automática das respostas (análise manual pelos autores);
- medição de aprendizagem ou desempenho acadêmico dos estudantes.

## 20. Stack final

```text
Frontend
└── Streamlit


Backend
└── FastAPI


Storage
└── Local (content/)


Database
└── PostgreSQL + pgvector


Document Processing
├── Docling
└── Python


Audio Transcription
└── Whisper (local, GPU)


Embeddings
└── Amazon Titan Text Embeddings V2 / AWS Bedrock


RAG
└── LangChain (text splitters)


Retrieval
└── pgvector


LLM
└── DeepSeek / AWS Bedrock


Infrastructure
└── Docker
```
