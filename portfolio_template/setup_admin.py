#!/usr/bin/env python3
"""
Simple script to create Django admin user
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_template.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin():
    """Create a simple admin user"""
    
    username = "admin"
    password = "admin123456"
    email = "vijaypardhu17@gmail.com"
    
    # Check if admin already exists
    if User.objects.filter(username=username).exists():
        print(f"✅ Admin user '{username}' already exists!")
        return True
    
    try:
        # Create admin user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name="Admin",
            last_name="User",
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        
        print(f"🎉 Admin user created successfully!")
        print(f"   Username: {username}")
        print(f"   Password: {password}")
        print(f"   Access admin at: /admin/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating admin: {e}")
        return False

if __name__ == "__main__":
    create_admin()
