#!/usr/bin/env python3
"""
Post-deployment script for Vijaya Pardhu Portfolio on Render
Run this script after your service is deployed and running
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append('/opt/render/project/src')

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_website.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.management import call_command

def main():
    print("🚀 Starting post-deployment setup...")
    
    try:
        # Populate initial data
        print("📊 Populating portfolio data...")
        call_command('populate_data')
        print("✅ Data population completed!")
        
        # Create superuser if it doesn't exist
        print("👤 Setting up superuser account...")
        username = 'vijayapardhu'
        email = 'vijaypardhu17@gmail.com'
        password = 'vijayapardhu2025'  # You can change this
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            print(f"✅ Superuser '{username}' created successfully!")
        else:
            print(f"⚠️  Superuser '{username}' already exists!")
            
        print("\n🎉 Post-deployment setup completed!")
        print(f"👤 Username: {username}")
        print(f"📧 Email: {email}")
        print(f"🔑 Password: {password}")
        print(f"🌐 Admin panel: /admin/")
        
    except Exception as e:
        print(f"❌ Error during post-deployment setup: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
