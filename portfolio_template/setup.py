#!/usr/bin/env python3
"""
Setup script for Django Portfolio Template
This script helps you get started with your portfolio website.
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def create_env_file():
    """Create .env file from template"""
    env_example = Path("env.example")
    env_file = Path(".env")
    
    if env_file.exists():
        print("⚠️  .env file already exists, skipping...")
        return True
    
    if not env_example.exists():
        print("❌ env.example file not found")
        return False
    
    print("📝 Creating .env file...")
    try:
        with open(env_example, 'r') as f:
            content = f.read()
        
        # Generate a random secret key
        import secrets
        secret_key = secrets.token_urlsafe(50)
        content = content.replace('your-secret-key-here', secret_key)
        
        with open(env_file, 'w') as f:
            f.write(content)
        
        print("✅ .env file created successfully")
        print("⚠️  Remember to update email settings in .env file")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Django Portfolio Template Setup")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("manage.py").exists():
        print("❌ Please run this script from the portfolio_template directory")
        sys.exit(1)
    
    # Create virtual environment
    if not Path("venv").exists():
        print("🐍 Creating virtual environment...")
        if not run_command("python -m venv venv", "Creating virtual environment"):
            sys.exit(1)
    
    # Activate virtual environment and install dependencies
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/macOS
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    # Install requirements
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies"):
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        sys.exit(1)
    
    # Run migrations
    if not run_command(f"{pip_cmd} install django", "Installing Django"):
        sys.exit(1)
    
    if not run_command("python manage.py makemigrations", "Creating migrations"):
        print("⚠️  Migration creation failed, but continuing...")
    
    if not run_command("python manage.py migrate", "Running migrations"):
        print("⚠️  Migration failed, but continuing...")
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("2. Create superuser:")
    print("   python manage.py createsuperuser")
    
    print("3. Run development server:")
    print("   python manage.py runserver")
    
    print("4. Visit http://127.0.0.1:8000/ to see your portfolio")
    print("5. Go to http://127.0.0.1:8000/admin/ to add content")
    
    print("\n📚 For detailed instructions, see README.md")
    print("🚀 Happy coding!")

if __name__ == "__main__":
    main()
