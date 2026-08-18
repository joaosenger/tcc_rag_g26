#!/bin/sh
set -e

echo "Inicializando banco de dados..."
python -m app.database.init_db

echo "Iniciando API..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
