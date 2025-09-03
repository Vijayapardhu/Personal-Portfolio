#!/usr/bin/env python3
"""
Script to load comprehensive portfolio data into the Django database
This script creates all the necessary data for a fully functional portfolio.
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_template.settings')
django.setup()

from main.models import Profile, Skill, Project, Achievement, SocialLink, SiteSettings, ContactMessage
from django.core.files.base import ContentFile

def load_portfolio_data():
    """Load comprehensive portfolio data into the database"""
    
    print("🚀 Loading Portfolio Data into Database")
    print("=" * 50)
    
    # 1. Create Site Settings
    print("\n📋 Creating Site Settings...")
    site_settings, created = SiteSettings.objects.get_or_create(
        defaults={
            'site_name': 'Vijaya Pardhu Portfolio',
            'hero_title': 'Hi, I\'m Vijaya Pardhu 👋',
            'hero_subtitle': 'Full-Stack Developer & Android Developer',
            'contact_email': 'vijaypardhu17@gmail.com',
            'primary_color': '#3B82F6',
            'secondary_color': '#8B5CF6',
            'accent_color': '#10B981',
        }
    )
    
    if created:
        print("✅ Created site settings")
    else:
        print("✅ Site settings already exist")
    
    # 2. Create Profile
    print("\n👤 Creating Profile...")
    profile, created = Profile.objects.get_or_create(
        defaults={
            'name': 'Vijaya Pardhu',
            'tagline': 'Full-Stack Developer & Android Developer',
            'about_text': 'I\'m a passionate developer with expertise in Android development, web technologies, and AI integration. I love building applications that solve real-world problems and create meaningful user experiences. With a strong foundation in Java, Python, and modern web technologies, I specialize in creating innovative solutions that combine cutting-edge AI capabilities with robust, user-friendly applications.',
            'email': 'vijaypardhu17@gmail.com',
            'phone': '+91 98765 43210',
            'location': 'India',
        }
    )
    
    if created:
        print("✅ Created profile")
    else:
        print("✅ Profile already exists")
    
    # 3. Create Skills
    print("\n🛠️ Creating Skills...")
    skills_data = [
        # Programming Languages
        {'name': 'Java', 'category': 'programming', 'proficiency': 90, 'icon_url': 'https://skillicons.dev/icons?i=java'},
        {'name': 'Python', 'category': 'programming', 'proficiency': 85, 'icon_url': 'https://skillicons.dev/icons?i=python'},
        {'name': 'JavaScript', 'category': 'programming', 'proficiency': 80, 'icon_url': 'https://skillicons.dev/icons?i=javascript'},
        {'name': 'PHP', 'category': 'programming', 'proficiency': 75, 'icon_url': 'https://skillicons.dev/icons?i=php'},
        
        # Frameworks & Libraries
        {'name': 'HTML', 'category': 'framework', 'proficiency': 95, 'icon_url': 'https://skillicons.dev/icons?i=html'},
        {'name': 'CSS', 'category': 'framework', 'proficiency': 90, 'icon_url': 'https://skillicons.dev/icons?i=css'},
        {'name': 'Django', 'category': 'framework', 'proficiency': 75, 'icon_url': 'https://skillicons.dev/icons?i=django'},
        {'name': 'Node.js', 'category': 'framework', 'proficiency': 70, 'icon_url': 'https://skillicons.dev/icons?i=nodejs'},
        
        # Tools & Platforms
        {'name': 'Android Studio', 'category': 'tool', 'proficiency': 85, 'icon_url': 'https://skillicons.dev/icons?i=androidstudio'},
        {'name': 'Git', 'category': 'tool', 'proficiency': 85, 'icon_url': 'https://skillicons.dev/icons?i=git'},
        {'name': 'Firebase', 'category': 'database', 'proficiency': 80, 'icon_url': 'https://skillicons.dev/icons?i=firebase'},
        {'name': 'MySQL', 'category': 'database', 'proficiency': 75, 'icon_url': 'https://skillicons.dev/icons?i=mysql'},
        
        # Specialized Technologies
        {'name': 'Porcupine', 'category': 'tool', 'proficiency': 70, 'icon_url': 'https://skillicons.dev/icons?i=code'},
        {'name': 'Google Gemini API', 'category': 'tool', 'proficiency': 75, 'icon_url': 'https://skillicons.dev/icons?i=code'},
        {'name': 'Playwright', 'category': 'tool', 'proficiency': 70, 'icon_url': 'https://skillicons.dev/icons?i=code'},
        {'name': 'OpenWeather API', 'category': 'tool', 'proficiency': 70, 'icon_url': 'https://skillicons.dev/icons?i=code'},
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
    
    # 4. Create Projects
    print("\n🚀 Creating Projects...")
    projects_data = [
        {
            'title': 'HeySara – AI Voice Assistant',
            'short_description': 'Offline + AI-powered Android assistant with hotword detection, speech recognition, and Google Gemini AI integration.',
            'description': 'HeySara is an advanced AI-powered voice assistant for Android that works offline and integrates with Google Gemini AI. It features hotword detection ("HeySara"), AI-powered responses, and task automation capabilities including opening apps and setting reminders. Built with Java and Android Studio, it showcases cutting-edge AI integration in mobile applications.',
            'tech_stack': ['Java', 'Android Studio', 'Firebase', 'Porcupine', 'Google Gemini API'],
            'github_link': 'https://github.com/Vijayapardhu/HeySara',
            'live_link': '',
            'featured': True,
        },
        {
            'title': 'College Management System',
            'short_description': 'Android + Web platform for college administration with QR attendance, tests, and dashboards.',
            'description': 'A comprehensive college management system that combines Android and web platforms for efficient college administration. Features include QR-based attendance tracking, online tests and results management, and comprehensive admin dashboards for student management. This project demonstrates full-stack development capabilities across multiple platforms.',
            'tech_stack': ['Java', 'Firebase', 'HTML', 'CSS', 'JavaScript'],
            'github_link': 'https://github.com/Vijayapardhu/College-Management-System',
            'live_link': '',
            'featured': True,
        },
        {
            'title': 'SBTET Results Clone',
            'short_description': 'Automated tool for fetching AP-SBTET results using scraping/automation scripts.',
            'description': 'An automated tool designed to fetch AP-SBTET results efficiently using web scraping and automation scripts. It provides a simple interface for users to access results quickly and reliably. Built with Node.js and Playwright, it showcases automation and web scraping expertise.',
            'tech_stack': ['Node.js', 'Playwright', 'JavaScript'],
            'github_link': 'https://github.com/Vijayapardhu/sbtetap-results',
            'live_link': '',
            'featured': False,
        },
        {
            'title': 'GiveGrip – Online Donation Platform',
            'short_description': 'Secure donation platform with Google login, OTP authentication, and payment integration.',
            'description': 'GiveGrip is a secure online donation platform that offers multiple authentication options including Google login and OTP verification. It features real-time donation tracking and secure payment integration for a seamless donation experience. Built with Django, it demonstrates modern web development practices and security implementation.',
            'tech_stack': ['Django', 'HTML', 'CSS', 'JavaScript', 'Firebase'],
            'github_link': 'https://github.com/Vijayapardhu/GiveGrip',
            'live_link': '',
            'featured': True,
        },
        {
            'title': 'Tourism Management System',
            'short_description': 'Web app for tourism package bookings with admin & user dashboards.',
            'description': 'A comprehensive tourism management system that allows users to book tourism packages with features like multi-language support, live maps integration, weather forecasting, and event scheduling for packages. Built with PHP and MySQL, it showcases traditional web development skills and database management.',
            'tech_stack': ['PHP', 'MySQL', 'HTML', 'CSS', 'JavaScript'],
            'github_link': 'https://github.com/Vijayapardhu/Tourism-Management-System',
            'live_link': '',
            'featured': False,
        },
        {
            'title': 'Church App',
            'short_description': 'Christian community app with Bible verses, prayers, and audio messages.',
            'description': 'A Christian community application that provides daily Bible quotes, prayer request submission functionality, and audio devotionals to help users in their spiritual journey. Built with Java and Firebase, it demonstrates mobile app development and cloud integration for community applications.',
            'tech_stack': ['Java', 'Android Studio', 'Firebase'],
            'github_link': 'https://github.com/Vijayapardhu/ChurchApp',
            'live_link': '',
            'featured': False,
        },
        {
            'title': 'Weather App',
            'short_description': 'A simple weather app fetching real-time weather info.',
            'description': 'A clean and simple weather application that fetches real-time weather information. It features city-based search functionality and provides accurate weather updates. Built with Java and OpenWeather API, it demonstrates API integration and clean UI design principles.',
            'tech_stack': ['Java', 'Android Studio', 'OpenWeather API'],
            'github_link': 'https://github.com/Vijayapardhu/WeatherApp',
            'live_link': '',
            'featured': False,
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
    
    # 5. Create Achievements
    print("\n🏆 Creating Achievements...")
    achievements_data = [
        {
            'title': 'AI Voice Assistant Development',
            'description': 'Successfully developed and deployed HeySara, an AI-powered voice assistant with Google Gemini integration.',
            'year': 2024,
            'icon': '🤖',
        },
        {
            'title': 'Full-Stack Web Development',
            'description': 'Completed multiple full-stack web applications including GiveGrip donation platform and Tourism Management System.',
            'year': 2024,
            'icon': '🌐',
        },
        {
            'title': 'Android App Development',
            'description': 'Developed and published multiple Android applications on Google Play Store.',
            'year': 2023,
            'icon': '📱',
        },
        {
            'title': 'Web Scraping & Automation',
            'description': 'Created automated tools for data extraction and results fetching using modern web technologies.',
            'year': 2023,
            'icon': '⚡',
        },
        {
            'title': 'Firebase Integration',
            'description': 'Successfully integrated Firebase services across multiple projects for authentication and data management.',
            'year': 2023,
            'icon': '🔥',
        },
    ]
    
    for achievement_data in achievements_data:
        achievement, created = Achievement.objects.get_or_create(
            title=achievement_data['title'],
            defaults=achievement_data
        )
        if created:
            print(f"✅ Created achievement: {achievement.title}")
    
    # 6. Create Social Links
    print("\n🔗 Creating Social Links...")
    social_links_data = [
        {
            'platform': 'github',
            'url': 'https://github.com/Vijayapardhu',
            'icon_class': 'fab fa-github',
            'order': 1,
        },
        {
            'platform': 'linkedin',
            'url': 'https://linkedin.com/in/vijayapardhu',
            'icon_class': 'fab fa-linkedin',
            'order': 2,
        },
        {
            'platform': 'twitter',
            'url': 'https://twitter.com/vijayapardhu',
            'icon_class': 'fab fa-twitter',
            'order': 3,
        },
    ]
    
    for social_data in social_links_data:
        social_link, created = SocialLink.objects.get_or_create(
            platform=social_data['platform'],
            defaults=social_data
        )
        if created:
            print(f"✅ Created social link: {social_link.get_platform_display()}")
    
    # 7. Create Sample Contact Messages (for demonstration)
    print("\n💬 Creating Sample Contact Messages...")
    sample_messages = [
        {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Project Collaboration Inquiry',
            'message': 'Hi Vijaya, I saw your portfolio and I\'m impressed with your work. I have a project that could benefit from your expertise. Would you be interested in discussing a potential collaboration?',
        },
        {
            'name': 'Sarah Smith',
            'email': 'sarah@techcompany.com',
            'subject': 'Job Opportunity',
            'message': 'Hello! We\'re looking for a talented developer with your skills. Your portfolio shows exactly the kind of experience we need. Are you currently open to new opportunities?',
        },
    ]
    
    for message_data in sample_messages:
        message, created = ContactMessage.objects.get_or_create(
            email=message_data['email'],
            subject=message_data['subject'],
            defaults=message_data
        )
        if created:
            print(f"✅ Created sample message: {message.subject}")
    
    # Summary
    print(f"\n🎉 Portfolio Data Loading Complete!")
    print("=" * 50)
    print(f"✅ Site Settings: 1")
    print(f"✅ Profile: 1")
    print(f"✅ Skills: {len(created_skills)}")
    print(f"✅ Projects: {len(created_projects)}")
    print(f"✅ Achievements: {len(achievements_data)}")
    print(f"✅ Social Links: {len(social_links_data)}")
    print(f"✅ Sample Messages: {len(sample_messages)}")
    
    print(f"\n🌐 Your portfolio is now ready with:")
    print(f"   • Professional profile and branding")
    print(f"   • 7 impressive projects with tech stacks")
    print(f"   • 16 technical skills with proficiency levels")
    print(f"   • 5 professional achievements")
    print(f"   • Social media links")
    print(f"   • Sample contact messages")
    
    print(f"\n🚀 Next steps:")
    print(f"   1. Run 'python create_admin.py' to create admin access")
    print(f"   2. Start Django server: 'python manage.py runserver'")
    print(f"   3. Visit your portfolio at: http://127.0.0.1:8000/")
    print(f"   4. Access admin at: http://127.0.0.1:8000/admin/")
    
    return True

if __name__ == '__main__':
    try:
        load_portfolio_data()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you have:")
        print("1. Run 'python manage.py migrate'")
        print("2. Django is properly configured")
