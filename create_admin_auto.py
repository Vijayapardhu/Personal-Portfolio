#!/usr/bin/env python3
"""
Automated script to create Django admin superuser
This script creates an admin user without user interaction for automated deployment.
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
from django.db import IntegrityError

def create_auto_admin():
    """Create an admin user automatically with preset credentials"""
    
    print("🔐 Creating Automated Admin User")
    print("=" * 40)
    
    # Default admin credentials
    username = "admin"
    email = "vijaypardhu17@gmail.com"
    password = "Admin@123456"
    
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
        print(f"   Email: {email}")
        print(f"   Is Superuser: {user.is_superuser}")
        print(f"   Is Staff: {user.is_staff}")
        
        print(f"\n⚠️  IMPORTANT: Change the password after first login!")
        print(f"   Access admin at: /admin/")
        
        return True
        
    except IntegrityError as e:
        print(f"❌ Error creating admin user: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def create_custom_admin(username, password, email="admin@example.com"):
    """Create a custom admin user with specified credentials"""
    
    print(f"🔐 Creating Custom Admin User: {username}")
    print("=" * 40)
    
    # Check if username already exists
    if User.objects.filter(username=username).exists():
        print(f"❌ Username '{username}' already exists!")
        return False
    
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
        
        print(f"🎉 Custom admin user '{username}' created successfully!")
        print(f"   Username: {username}")
        print(f"   Email: {email}")
        print(f"   Is Superuser: {user.is_superuser}")
        print(f"   Is Staff: {user.is_staff}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating custom admin: {e}")
        return False

def main():
    """Main function - can be called with command line arguments"""
    
    if len(sys.argv) > 1:
        # Command line mode
        if sys.argv[1] == "custom" and len(sys.argv) >= 4:
            username = sys.argv[2]
            password = sys.argv[3]
            email = sys.argv[4] if len(sys.argv) > 4 else "admin@example.com"
            create_custom_admin(username, password, email)
        else:
            print("Usage: python create_admin_auto.py [custom <username> <password> [email]]")
            print("Examples:")
            print("  python create_admin_auto.py                    # Create default admin")
            print("  python create_admin_auto.py custom myuser mypass123  # Create custom admin")
    else:
        # Default mode - create standard admin
        create_auto_admin()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure Django is properly configured and migrations are applied.")
