#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python load_portfolio_data.py
python create_admin_auto.py
