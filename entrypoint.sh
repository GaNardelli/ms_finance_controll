#!/bin/sh

# Aborta o script se qualquer comando falhar
set -e

# Espera o banco de dados (serviço 'db') estar pronto na porta 3306.
# O comando 'nc' (netcat) verifica se a porta está aberta.
echo "Aguardando o banco de dados..."
while ! nc -z db 3306; do
  sleep 0.1
done
echo "Banco de dados iniciado."

# Executa o comando para criar as tabelas.
# O comando 'flask init-db' foi definido no app.py.
echo "Criando tabelas do banco de dados..."
flask init-db

# Executa o comando principal do contêiner (o CMD do Dockerfile).
exec "$@"