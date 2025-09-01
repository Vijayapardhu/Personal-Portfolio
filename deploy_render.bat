@echo off
REM Render Deployment Script for Vijaya Pardhu Portfolio (Windows)
REM This script sets up the database and creates necessary users

echo 🚀 Starting Render deployment setup...

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

REM Collect static files
echo 🎨 Collecting static files...
python manage.py collectstatic --no-input

REM Run database migrations
echo 🗄️ Running database migrations...
python manage.py migrate

REM Populate initial data
echo 📊 Populating portfolio data...
python manage.py populate_data

REM Create superuser if it doesn't exist
echo 👤 Setting up superuser account...
if "%DJANGO_SUPERUSER_PASSWORD%"=="" (
    echo ⚠️  DJANGO_SUPERUSER_PASSWORD not set, using default password
    set DJANGO_SUPERUSER_PASSWORD=vijayapardhu2024!
)

python manage.py create_render_superuser --username vijayapardhu --email vijaypardhu17@gmail.com

echo ✅ Deployment setup completed successfully!
echo 🌐 Your portfolio is ready locally at: http://127.0.0.1:8000/
echo 🔐 Admin panel: http://127.0.0.1:8000/admin/
echo 👤 Username: vijayapardhu
echo 📧 Email: vijaypardhu17@gmail.com
echo 🔑 Password: Check your environment variables or use the default

pause
