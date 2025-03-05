FROM python:3.12-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

COPY . /app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.uuid_assignment.app:app", "--host", "0.0.0.0", "--port", "8000"]





