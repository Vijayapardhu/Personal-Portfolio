#!/usr/bin/env python3
"""
Script to create Django admin superuser for the portfolio
This script can be run locally or on Render to set up admin access.
"""

import os
import sys
import django
from getpass import getpass

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_template.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.management import call_command
from django.db import IntegrityError

def create_superuser():
    """Create a Django superuser for admin access"""
    
    print("🔐 Creating Django Admin Superuser")
    print("=" * 40)
    
    # Check if superuser already exists
    if User.objects.filter(is_superuser=True).exists():
        print("✅ Superuser already exists!")
        existing_admin = User.objects.filter(is_superuser=True).first()
        print(f"   Username: {existing_admin.username}")
        print(f"   Email: {existing_admin.email}")
        print(f"   Is Active: {existing_admin.is_active}")
        
        choice = input("\n❓ Do you want to create another superuser? (y/N): ").lower()
        if choice != 'y':
            print("👋 No new superuser created. Exiting...")
            return
    
    print("\n📝 Enter admin user details:")
    
    # Get username
    while True:
        username = input("Username (default: admin): ").strip()
        if not username:
            username = "admin"
        
        if User.objects.filter(username=username).exists():
            print(f"❌ Username '{username}' already exists. Please choose another.")
            continue
        break
    
    # Get email
    while True:
        email = input("Email (default: admin@example.com): ").strip()
        if not email:
            email = "admin@example.com"
        
        if User.objects.filter(email=email).exists():
            print(f"❌ Email '{email}' already exists. Please choose another.")
            continue
        break
    
    # Get password
    while True:
        password = getpass("Password: ")
        if len(password) < 8:
            print("❌ Password must be at least 8 characters long.")
            continue
        
        confirm_password = getpass("Confirm Password: ")
        if password != confirm_password:
            print("❌ Passwords don't match. Please try again.")
            continue
        break
    
    # Get first and last name
    first_name = input("First Name (optional): ").strip()
    last_name = input("Last Name (optional): ").strip()
    
    try:
        # Create the superuser
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        
        print(f"\n🎉 Superuser '{username}' created successfully!")
        print(f"   Username: {username}")
        print(f"   Email: {email}")
        print(f"   Full Name: {first_name} {last_name}".strip())
        print(f"   Is Superuser: {user.is_superuser}")
        print(f"   Is Staff: {user.is_staff}")
        print(f"   Is Active: {user.is_active}")
        
        print(f"\n🌐 You can now:")
        print(f"   1. Access admin panel at: /admin/")
        print(f"   2. Login with username: {username}")
        print(f"   3. Manage your portfolio content")
        
    except IntegrityError as e:
        print(f"❌ Error creating superuser: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    
    return True

def create_default_admin():
    """Create a default admin user with preset credentials"""
    
    print("🔐 Creating Default Admin User")
    print("=" * 40)
    
    default_username = "admin"
    default_email = "admin@example.com"
    default_password = "admin123456"
    
    # Check if default admin already exists
    if User.objects.filter(username=default_username).exists():
        print(f"✅ Default admin '{default_username}' already exists!")
        return True
    
    try:
        # Create default admin user
        user = User.objects.create_user(
            username=default_username,
            email=default_email,
            password=default_password,
            first_name="Admin",
            last_name="User",
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        
        print(f"🎉 Default admin user created successfully!")
        print(f"   Username: {default_username}")
        print(f"   Password: {default_password}")
        print(f"   Email: {default_email}")
        
        print(f"\n⚠️  IMPORTANT: Change the default password after first login!")
        print(f"   Default credentials are for development only!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating default admin: {e}")
        return False

def list_users():
    """List all existing users"""
    
    print("👥 Existing Users")
    print("=" * 40)
    
    users = User.objects.all().order_by('date_joined')
    
    if not users.exists():
        print("No users found.")
        return
    
    for user in users:
        status = []
        if user.is_superuser:
            status.append("Superuser")
        if user.is_staff:
            status.append("Staff")
        if user.is_active:
            status.append("Active")
        else:
            status.append("Inactive")
        
        print(f"   {user.username} ({user.email}) - {', '.join(status)}")

def main():
    """Main function to run the admin creation script"""
    
    print("🚀 Django Portfolio Admin Setup")
    print("=" * 50)
    
    while True:
        print("\n📋 Choose an option:")
        print("1. Create custom superuser")
        print("2. Create default admin (admin/admin123456)")
        print("3. List existing users")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            create_superuser()
        elif choice == "2":
            create_default_admin()
        elif choice == "3":
            list_users()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")
        
        if choice in ["1", "2"]:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Script interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Make sure you have:")
        print("1. Run 'python manage.py migrate'")
        print("2. The Django server is running")
