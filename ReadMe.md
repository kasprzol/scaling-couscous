# Info
A simple REST API webapp with two endpoints:
- ping
- info

The app uses FastAPI as the web framework and _aiohttp_ for fetching remote resources.

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

    docker run --rm web_pinger --publish 8000:8000

