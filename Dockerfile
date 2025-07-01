FROM python:3.13.5-alpine3.22

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "app.py", "--debug", "run", "--host=0.0.0.0"]