#!/usr/bin/env python3
"""
Script to reset admin password and create new admin user
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

def reset_admin():
    """Reset admin password or create new admin user"""
    
    print("🔐 Admin Password Reset")
    print("=" * 30)
    
    # New secure credentials
    username = "admin"
    new_password = "Portfolio@2024!"
    email = "admin@portfolio.com"
    
    try:
        # Try to get existing admin user
        try:
            user = User.objects.get(username=username)
            print(f"✅ Found existing admin user: {username}")
            
            # Reset password
            user.set_password(new_password)
            user.email = email
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            
            print(f"🔄 Password reset successfully!")
            
        except User.DoesNotExist:
            # Create new admin user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=new_password,
                first_name="Portfolio",
                last_name="Admin",
                is_staff=True,
                is_superuser=True,
                is_active=True
            )
            print(f"🎉 New admin user created successfully!")
        
        print(f"\n📋 Admin Credentials:")
        print(f"   Username: {username}")
        print(f"   Password: {new_password}")
        print(f"   Email: {email}")
        print(f"\n🌐 Access admin panel at: /admin/")
        print(f"⚠️  Please change the password after first login!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    reset_admin()