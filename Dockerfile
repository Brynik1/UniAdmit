FROM python:3.11-slim

WORKDIR /app

# Копирование requirements и установка зависимостей
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирование исходного кода
COPY . .

# Открытие порта
EXPOSE 8000