FROM python:3.10

RUN python3 -m pip install -U pip wheel poetry
RUN poetry config virtualenvs.in-project true
RUN mkdir -p /srv/webpinger
WORKDIR /srv/webpinger
COPY ../poetry.lock /srv/webpinger
COPY ../pyproject.toml /srv/webpinger
RUN poetry install --no-root  --no-dev
# the lines above are usually cached. The ones below will be rebuild everytime.
COPY .. /srv/webpinger
RUN poetry install --no-dev

EXPOSE 8000

ENTRYPOINT ["/srv/webpinger/docker/webapp_entrypoint.sh"]