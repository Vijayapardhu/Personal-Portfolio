#!/usr/bin/env bash
# Render Deployment Script for Vijaya Pardhu Portfolio
# This script sets up the database and creates necessary users

set -e  # Exit on any error

echo "🚀 Starting Render deployment setup..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --no-input

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Populate initial data
echo "📊 Populating portfolio data..."
python manage.py populate_data

# Create superuser if it doesn't exist
echo "👤 Setting up superuser account..."
if [ -z "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "⚠️  DJANGO_SUPERUSER_PASSWORD not set, using default password"
    export DJANGO_SUPERUSER_PASSWORD="vijayapardhu2024!"
fi

python manage.py create_render_superuser \
    --username vijayapardhu \
    --email vijaypardhu17@gmail.com

echo "✅ Deployment setup completed successfully!"
echo "🌐 Your portfolio is ready at: https://vijaya-pardhu-portfolio.onrender.com"
echo "🔐 Admin panel: https://vijaya-pardhu-portfolio.onrender.com/admin/"
echo "👤 Username: vijayapardhu"
echo "📧 Email: vijaypardhu17@gmail.com"
echo "🔑 Password: Check your Render environment variables"
