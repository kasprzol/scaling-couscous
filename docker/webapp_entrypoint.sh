#!/bin/bash

set -euxo pipefail

# In production this would be at least a number of uwsgi/gunicorn processes
# behind a proxy like nginx or haproxy.
poetry run uvicorn --host 0.0.0.0 webapp.main:app