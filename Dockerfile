FROM python:3.11.4-slim

ENV YOURHELPER_HOME /yourhelper

WORKDIR $YOURHELPER_HOME

COPY pyproject.toml $YOURHELPER_HOME/pyproject.toml
COPY poetry.lock $YOURHELPER_HOME/poetry.lock

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --only main

ENV PYTHONPATH "/yourhelper/${PYTHONPATH}"

COPY . .

ENTRYPOINT ["python", "yourhelper/main.py"]