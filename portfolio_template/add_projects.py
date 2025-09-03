#!/usr/bin/env python3
"""
Script to add sample projects to the Django portfolio database.
Run this script after setting up the database and creating a superuser.
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_template.settings')
django.setup()

from main.models import Project, Skill, Profile, SiteSettings
from django.core.files.base import ContentFile

def create_sample_data():
    """Create sample data for the portfolio"""
    
    print("🚀 Creating sample portfolio data...")
    
    # Create or get site settings
    site_settings, created = SiteSettings.objects.get_or_create(
        defaults={
            'site_name': 'Pardhu Portfolio',
            'hero_title': 'Hi, I\'m Pardhu 👋',
            'hero_subtitle': 'Full-Stack Developer & Android Developer',
            'contact_email': 'pardhu@example.com',
            'primary_color': '#3B82F6',
            'secondary_color': '#8B5CF6',
            'accent_color': '#10B981',
        }
    )
    
    if created:
        print("✅ Created site settings")
    else:
        print("✅ Site settings already exist")
    
    # Create or get profile
    profile, created = Profile.objects.get_or_create(
        defaults={
            'name': 'Pardhu',
            'tagline': 'Full-Stack Developer & Android Developer',
            'about_text': 'Passionate developer with expertise in Android development, web technologies, and AI integration.',
            'email': 'pardhu@example.com',
            'phone': '+91 98765 43210',
            'location': 'India',
        }
    )
    
    if created:
        print("✅ Created profile")
    else:
        print("✅ Profile already exists")
    
    # Create sample skills
    skills_data = [
        {'name': 'Java', 'category': 'programming', 'proficiency': 90, 'icon_url': 'https://skillicons.dev/icons?i=java'},
        {'name': 'Python', 'category': 'programming', 'proficiency': 85, 'icon_url': 'https://skillicons.dev/icons?i=python'},
        {'name': 'JavaScript', 'category': 'programming', 'proficiency': 80, 'icon_url': 'https://skillicons.dev/icons?i=javascript'},
        {'name': 'HTML', 'category': 'framework', 'proficiency': 95, 'icon_url': 'https://skillicons.dev/icons?i=html'},
        {'name': 'CSS', 'category': 'framework', 'proficiency': 90, 'icon_url': 'https://skillicons.dev/icons?i=css'},
        {'name': 'Django', 'category': 'framework', 'proficiency': 75, 'icon_url': 'https://skillicons.dev/icons?i=django'},
        {'name': 'Android Studio', 'category': 'tool', 'proficiency': 85, 'icon_url': 'https://skillicons.dev/icons?i=androidstudio'},
        {'name': 'Firebase', 'category': 'database', 'proficiency': 80, 'icon_url': 'https://skillicons.dev/icons?i=firebase'},
        {'name': 'MySQL', 'category': 'database', 'proficiency': 75, 'icon_url': 'https://skillicons.dev/icons?i=mysql'},
        {'name': 'Node.js', 'category': 'framework', 'proficiency': 70, 'icon_url': 'https://skillicons.dev/icons?i=nodejs'},
        {'name': 'PHP', 'category': 'programming', 'proficiency': 75, 'icon_url': 'https://skillicons.dev/icons?i=php'},
        {'name': 'Git', 'category': 'tool', 'proficiency': 85, 'icon_url': 'https://skillicons.dev/icons?i=git'},
    ]
    
    created_skills = []
    for skill_data in skills_data:
        skill, created = Skill.objects.get_or_create(
            name=skill_data['name'],
            defaults=skill_data
        )
        if created:
            print(f"✅ Created skill: {skill.name}")
        created_skills.append(skill)
    
    # Create sample projects
    projects_data = [
        {
            'title': 'HeySara – AI Voice Assistant',
            'short_description': 'Offline + AI-powered Android assistant with hotword detection, speech recognition, and Google Gemini AI integration.',
            'description': 'HeySara is an advanced AI-powered voice assistant for Android that works offline and integrates with Google Gemini AI. It features hotword detection ("HeySara"), AI-powered responses, and task automation capabilities including opening apps and setting reminders.',
            'tech_stack': ['Java', 'Android Studio', 'Firebase', 'Porcupine', 'Google Gemini API'],
            'github_link': 'https://github.com/pardhu/HeySara',
            'live_link': '',
            'featured': True,
            'image': None,
        },
        {
            'title': 'College Management System',
            'short_description': 'Android + Web platform for college administration with QR attendance, tests, and dashboards.',
            'description': 'A comprehensive college management system that combines Android and web platforms for efficient college administration. Features include QR-based attendance tracking, online tests and results management, and comprehensive admin dashboards for student management.',
            'tech_stack': ['Java', 'Firebase', 'HTML', 'CSS', 'JavaScript'],
            'github_link': 'https://github.com/pardhu/College-Management-System',
            'live_link': '',
            'featured': True,
            'image': None,
        },
        {
            'title': 'SBTET Results Clone',
            'short_description': 'Automated tool for fetching AP-SBTET results using scraping/automation scripts.',
            'description': 'An automated tool designed to fetch AP-SBTET results efficiently using web scraping and automation scripts. It provides a simple interface for users to access results quickly and reliably.',
            'tech_stack': ['Node.js', 'Playwright', 'JavaScript'],
            'github_link': 'https://github.com/pardhu/sbtetap-results',
            'live_link': '',
            'featured': False,
            'image': None,
        },
        {
            'title': 'GiveGrip – Online Donation Platform',
            'short_description': 'Secure donation platform with Google login, OTP authentication, and payment integration.',
            'description': 'GiveGrip is a secure online donation platform that offers multiple authentication options including Google login and OTP verification. It features real-time donation tracking and secure payment integration for a seamless donation experience.',
            'tech_stack': ['Django', 'HTML', 'CSS', 'JavaScript', 'Firebase'],
            'github_link': 'https://github.com/pardhu/GiveGrip',
            'live_link': '',
            'featured': True,
            'image': None,
        },
        {
            'title': 'Tourism Management System',
            'short_description': 'Web app for tourism package bookings with admin & user dashboards.',
            'description': 'A comprehensive tourism management system that allows users to book tourism packages with features like multi-language support, live maps integration, weather forecasting, and event scheduling for packages.',
            'tech_stack': ['PHP', 'MySQL', 'HTML', 'CSS', 'JavaScript'],
            'github_link': 'https://github.com/pardhu/Tourism-Management-System',
            'live_link': '',
            'featured': False,
            'image': None,
        },
        {
            'title': 'Church App',
            'short_description': 'Christian community app with Bible verses, prayers, and audio messages.',
            'description': 'A Christian community application that provides daily Bible quotes, prayer request submission functionality, and audio devotionals to help users in their spiritual journey.',
            'tech_stack': ['Java', 'Android Studio', 'Firebase'],
            'github_link': 'https://github.com/pardhu/ChurchApp',
            'live_link': '',
            'featured': False,
            'image': None,
        },
        {
            'title': 'Weather App',
            'short_description': 'A simple weather app fetching real-time weather info.',
            'description': 'A clean and simple weather application that fetches real-time weather information. It features city-based search functionality and provides accurate weather updates.',
            'tech_stack': ['Java', 'Android Studio', 'OpenWeather API'],
            'github_link': 'https://github.com/pardhu/WeatherApp',
            'live_link': '',
            'featured': False,
            'image': None,
        },
    ]
    
    created_projects = []
    for project_data in projects_data:
        # Get tech stack skills
        tech_stack_skills = []
        for tech_name in project_data['tech_stack']:
            try:
                skill = Skill.objects.get(name__iexact=tech_name)
                tech_stack_skills.append(skill)
            except Skill.DoesNotExist:
                # Create skill if it doesn't exist
                skill = Skill.objects.create(
                    name=tech_name,
                    category='tool',
                    proficiency=70,
                    icon_url='https://skillicons.dev/icons?i=code'
                )
                print(f"✅ Created missing skill: {skill.name}")
                tech_stack_skills.append(skill)
        
        # Remove tech_stack from project_data before creating project
        tech_stack = project_data.pop('tech_stack')
        
        project, created = Project.objects.get_or_create(
            title=project_data['title'],
            defaults=project_data
        )
        
        if created:
            print(f"✅ Created project: {project.title}")
        else:
            print(f"✅ Project already exists: {project.title}")
        
        # Add tech stack skills
        project.tech_stack.set(tech_stack_skills)
        created_projects.append(project)
    
    print(f"\n🎉 Successfully created:")
    print(f"   • {len(created_skills)} skills")
    print(f"   • {len(created_projects)} projects")
    print(f"   • 1 profile")
    print(f"   • 1 site settings")
    
    print(f"\n🌐 You can now:")
    print(f"   1. Visit http://127.0.0.1:8000/ to see your portfolio")
    print(f"   2. Visit http://127.0.0.1:8000/admin/ to manage content")
    print(f"   3. Customize colors, text, and content through the admin panel")

if __name__ == '__main__':
    try:
        create_sample_data()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you have:")
        print("1. Run 'python manage.py migrate'")
        print("2. Created a superuser with 'python manage.py createsuperuser'")
        print("3. The Django server is running")
