# Evaluation

Código de avaliação experimental do projeto (LLM puro vs. LLM+RAG).

## Estrutura

- `datasets/questions.json`: dataset de perguntas com respostas de referência e trechos relevantes (gabarito);
- `results/`: saídas dos experimentos (não versionado);
- `run_eval.py`: executa o dataset nas duas condições e salva as respostas em `results/`;
- `metrics.py`: calcula Precision@K e Recall@K da recuperação.

## Execução

```bash
python evaluation/run_eval.py
python evaluation/metrics.py
```

A classificação manual das respostas (correta / parcialmente correta / incorreta) é realizada pelos três avaliadores a partir dos arquivos salvos em `results/`.
