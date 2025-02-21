FROM python:3.12-slim

WORKDIR /app

RUN pip install uv
COPY pyproject.toml .
RUN uv pip install -e .[dev]

COPY . .

CMD ["pytest"]