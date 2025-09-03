#!/usr/bin/env python3
"""
Setup script for Django Portfolio Template
This script automates the initial setup process.
"""

import os
import sys
import subprocess
import platform
import secrets
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors gracefully."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 13:
        print("⚠️  Warning: Python 3.13+ detected. Some packages may have compatibility issues.")
        print("💡 Consider using Python 3.9-3.11 for better compatibility.")
        return False
    elif version.major == 3 and version.minor >= 8:
        print("✅ Python version is compatible")
        return True
    else:
        print("❌ Python 3.8+ is required")
        return False

def create_env_file():
    """Create .env file with required environment variables."""
    env_file = Path('.env')
    if env_file.exists():
        print("📝 .env file already exists, skipping creation")
        return True
    
    print("📝 Creating .env file...")
    
    # Generate a secure secret key
    secret_key = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
    
    env_content = f"""# Django Settings
SECRET_KEY={secret_key}
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email Settings (configure these for production)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
"""
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def install_dependencies():
    """Install Python dependencies with fallback options."""
    print("\n📦 Installing dependencies...")
    
    # Try the main requirements first
    if run_command("pip install -r requirements.txt", "Installing main requirements"):
        return True
    
    print("\n⚠️  Main requirements failed, trying compatible versions...")
    
    # Try the compatible requirements
    if run_command("pip install -r requirements-compatible.txt", "Installing compatible requirements"):
        return True
    
    print("\n⚠️  Compatible requirements failed, trying individual packages...")
    
    # Try installing packages individually with flexible versions
    packages = [
        "Django>=4.2.0",
        "Pillow>=9.5.0",
        "gunicorn",
        "whitenoise",
        "python-decouple",
        "django-crispy-forms",
        "crispy-tailwind"
    ]
    
    for package in packages:
        if not run_command(f"pip install {package}", f"Installing {package}"):
            print(f"⚠️  Failed to install {package}, continuing...")
    
    return True

def main():
    """Main setup function."""
    print("🚀 Django Portfolio Template Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        print("\n❌ Setup cannot continue due to Python version incompatibility")
        print("💡 Please use Python 3.8-3.11 for best compatibility")
        return
    
    # Create virtual environment
    if not run_command("python -m venv venv", "Creating virtual environment"):
        print("❌ Failed to create virtual environment")
        return
    
    # Activate virtual environment
    if platform.system() == "Windows":
        activate_script = "venv\\Scripts\\activate"
        print(f"\n💡 To activate virtual environment, run: {activate_script}")
        print("💡 Then run: pip install -r requirements.txt")
    else:
        activate_script = "source venv/bin/activate"
        print(f"\n💡 To activate virtual environment, run: {activate_script}")
        print("💡 Then run: pip install -r requirements.txt")
    
    # Create .env file
    create_env_file()
    
    print("\n" + "=" * 40)
    print("🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Activate virtual environment:")
    print(f"   {activate_script}")
    print("2. Install dependencies:")
    print("   pip install -r requirements.txt")
    print("3. Run migrations:")
    print("   python manage.py migrate")
    print("4. Create superuser:")
    print("   python manage.py createsuperuser")
    print("5. Run development server:")
    print("   python manage.py runserver")
    print("\n💡 If you encounter package compatibility issues:")
    print("   - Try: pip install -r requirements-compatible.txt")
    print("   - Or install packages individually with flexible versions")
    print("   - Consider using Python 3.9-3.11 for better compatibility")

if __name__ == "__main__":
    main()
