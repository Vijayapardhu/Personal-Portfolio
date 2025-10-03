#!/bin/bash

# Start script for Render deployment
set -e

echo "Starting Django application..."

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create admin user if needed
python create_admin_auto.py || echo "Admin user creation skipped"

# Start Gunicorn
exec gunicorn portfolio_template.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -