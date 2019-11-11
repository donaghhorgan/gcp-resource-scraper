# Firestore Resource Scraper

Scrapes web resources and persists them to Google Cloud Firestore.

## Prerequisites

### Dependencies

Dependencies are managed with [pipenv](https://pipenv.readthedocs.io/en/latest/). Run `pipenv install` to create a virtual environment with the packages you need to run the pipeline.

### Google Cloud credentials

[Create credentials](https://cloud.google.com/docs/authentication/) for Google Cloud Firestore and save them to `credentials.json`.

### Configuration

Create a file containing the scraper configuration. See [`config/cork-parking.yml`](./config/cork-parking.yml) for an example. 

## Usage

Build and run with Docker:

```
docker build -t gcp-resource-scraper .
docker run -it --rm -v <CREDENTIALS_FILE>:/app/credentials.json -v <CONFIG_FILE>:/app/config.yml gcp-resource-scraper
```