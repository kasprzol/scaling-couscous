# Introduction
A simple REST API webapp with two endpoints:
- ping
- info

The app uses FastAPI as the web framework and _aiohttp_ for fetching remote resources.

## Example usage

### Info

```shell
curl -X 'GET' 'http://127.0.0.1:8000/info' -H 'accept: application/json'
```
### Ping

```shell
curl -X 'POST' 'http://127.0.0.1:8000/ping' \
  -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d '{"url": "http://info.cern.ch/hypertext/WWW/TheProject.html"}'
```

# Installation

    poetry install

# Running

    poetry run uvicorn webapp.main:app --host 0.0.0.0

# testing

    poetry run pytest

# swagger
Run the webapp, then go to http://localhost:8000/docs#/

# Docker

## Create the docker image:

    docker build -f docker/Dockerfile --tag web_pinger .

## Run docker container:

    docker run --publish 8000:8000 --rm web_pinger

