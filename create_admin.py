#!/usr/bin/env python3
"""
Create Additional Admin User Script
Creates an admin user with username 'admin' and password 'admin123'
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

def create_admin_user():
    print("👤 Creating additional admin user...")
    
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123'
    
    try:
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            print(f"⚠️  User '{username}' already exists!")
            
            # Update password if user exists
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            print(f"✅ Updated existing user '{username}' with new password!")
            
        else:
            # Create new superuser
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            print(f"✅ Successfully created admin user '{username}'!")
        
        print(f"\n🔐 Admin Account Details:")
        print(f"   Username: {username}")
        print(f"   Email: {email}")
        print(f"   Password: {password}")
        print(f"   Access Level: Superuser (Full Admin)")
        print(f"   Admin Panel: /admin/")
        
    except Exception as e:
        print(f"❌ Error creating admin user: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    create_admin_user()
