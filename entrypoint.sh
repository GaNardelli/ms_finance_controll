#!/bin/sh

# Aborta o script se qualquer comando falhar
set -e

# Executa o comando para criar as tabelas.
# O comando 'flask init-db' foi definido no app.py.
echo "Criando tabelas do banco de dados..."
flask init-db

# Executa o comando principal do contêiner (o CMD do Dockerfile).
exec "$@"