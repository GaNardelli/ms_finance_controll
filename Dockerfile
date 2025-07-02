FROM python:3.13.5-alpine3.22

WORKDIR /app

# Instala dependências do sistema, incluindo o netcat para o entrypoint.
RUN apk add --no-cache netcat-openbsd

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copia o script de entrada e o torna executável
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 5000

# Define o script de entrada e o comando padrão para iniciar a aplicação
ENTRYPOINT ["./entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]