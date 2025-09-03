#!/usr/bin/env python3
"""
Deployment script for Django Portfolio Template on Render
This script helps prepare the project for production deployment.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors gracefully."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def prepare_for_deployment():
    """Prepare the project for deployment on Render."""
    print("🚀 Preparing Django Portfolio Template for Render deployment...")
    
    # Check if we're in the right directory
    if not Path("manage.py").exists():
        print("❌ Error: Please run this script from the project root directory")
        return False
    
    # Create .env file for local development
    env_content = """# Local Development Environment Variables
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    print("✅ Created .env file for local development")
    
    # Run Django checks
    if not run_command("python manage.py check --deploy", "Running Django deployment checks"):
        return False
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        return False
    
    # Create a superuser if none exists
    print("🔐 To create a superuser for admin access, run:")
    print("   python manage.py createsuperuser")
    
    print("\n🎉 Project is ready for deployment!")
    print("\n📋 Next steps:")
    print("1. Push your code to GitHub/GitLab")
    print("2. Connect your repository to Render")
    print("3. Render will automatically deploy using render.yaml")
    print("4. Set environment variables in Render dashboard")
    print("5. Your portfolio will be live at: https://portfolio-template.onrender.com")
    
    return True

if __name__ == "__main__":
    prepare_for_deployment()
