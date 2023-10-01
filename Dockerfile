# Docker-команда FROM указывает базовый образ контейнера
# Наш базовый образ - это Linux с предустановленным python-3.10
FROM python:3.11.3

# Установим переменную окружения
ENV YOURHELPER_HOME /yourhelper

# Установим рабочую директорию внутри контейнера
WORKDIR $YOURHELPER_HOME

# Скопируем остальные файлы в рабочую директорию контейнера
COPY pyproject.toml $YOURHELPER_HOME/pyproject.toml
COPY poetry.lock $YOURHELPER_HOME/poetry.lock

# Установим зависимости внутри контейнера
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --only main

# Обозначим порт где работает приложение внутри контейнера
ENV PYTHONPATH "/yourhelper/${PYTHONPATH}"

COPY . .

# Запустим наше приложение внутри контейнера
ENTRYPOINT ["python", "yourhelper/main.py"]