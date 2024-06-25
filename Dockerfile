# Используем официальный образ Python
FROM python:3.12.1-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . /app

# Устанавливаем зависимости, если у вас есть файл requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8000 для доступа к вашему приложению
EXPOSE 8000

# Команда для запуска вашего сервера
CMD ["python", "serve_with_cache.py"]
