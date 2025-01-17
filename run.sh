#!/bin/sh

export PYTHONPATH=$(pwd)
export FLASK_APP=src/main.py

alembic upgrade head

python3 src/infra/database/seeder/seed_users.py

flask run --host=0.0.0.0 --port=5000