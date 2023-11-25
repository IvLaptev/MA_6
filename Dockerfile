FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /code

# Установка зависимостей проекта
COPY ./requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Перенос проекта в образ
COPY ./app /code/app

# Копирование файлов alembic
COPY ./alembic.ini /code/alembic.ini

EXPOSE 8000

CMD ["/bin/sh", "-c", \
    "alembic upgrade head" && \
    "uvicorn student_service.api.main:app --host 0.0.0.0 --port 80"]
