FROM python:3.7-slim

ENV PYTHONUNBUFFERED=TRUE \
    PYTHONDONTWRITEBYTECODE=TRUE \
    PIP_NO_CACHE_DIR=off \
    GOOGLE_APPLICATION_CREDENTIALS=credentials.json

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && \
    pipenv install --system && \
    rm -rf /var/lib/apt/lists/*

COPY . ./

ENTRYPOINT ["python", "app.py"]
CMD ["config.yml"]