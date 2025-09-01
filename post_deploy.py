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
        
        # Create first superuser if it doesn't exist
        print("👤 Setting up first superuser account...")
        username1 = 'vijayapardhu'
        email1 = 'vijaypardhu17@gmail.com'
        password1 = 'vijayapardhu2025'  # You can change this
        
        if not User.objects.filter(username=username1).exists():
            User.objects.create_superuser(username1, email1, password1)
            print(f"✅ Superuser '{username1}' created successfully!")
        else:
            print(f"⚠️  Superuser '{username1}' already exists!")
        
        # Create second admin user if it doesn't exist
        print("👤 Setting up second admin account...")
        username2 = 'admin'
        email2 = 'admin@example.com'
        password2 = 'admin123'
        
        if not User.objects.filter(username=username2).exists():
            User.objects.create_superuser(username2, email2, password2)
            print(f"✅ Admin user '{username2}' created successfully!")
        else:
            print(f"⚠️  Admin user '{username2}' already exists!")
            
        print("\n🎉 Post-deployment setup completed!")
        print(f"\n🔐 Admin Account 1:")
        print(f"   Username: {username1}")
        print(f"   Email: {email1}")
        print(f"   Password: {password1}")
        
        print(f"\n🔐 Admin Account 2:")
        print(f"   Username: {username2}")
        print(f"   Email: {email2}")
        print(f"   Password: {password2}")
        
        print(f"\n🌐 Admin panel: /admin/")
        
    except Exception as e:
        print(f"❌ Error during post-deployment setup: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
