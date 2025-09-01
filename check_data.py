#!/usr/bin/env python3
"""
Data Check Script for Vijaya Pardhu Portfolio
Run this to see what data exists in your database
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append('/opt/render/project/src')

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_website.settings')
django.setup()

from portfolio.models import Project, Achievement, Skill, Hobby, ContactInfo, ProfileStats, Education, Experience, Certification
from django.contrib.auth.models import User

def check_data():
    print("🔍 Checking database data...")
    print("=" * 50)
    
    # Check Users
    users = User.objects.all()
    print(f"👥 Users: {users.count()}")
    for user in users:
        print(f"   - {user.username} ({user.email}) - {'Superuser' if user.is_superuser else 'Regular user'}")
    
    # Check Contact Info
    contacts = ContactInfo.objects.all()
    print(f"\n📞 Contact Info: {contacts.count()}")
    for contact in contacts:
        print(f"   - {contact.email} | {contact.github_username} | {contact.location}")
    
    # Check Profile Stats
    stats = ProfileStats.objects.all()
    print(f"\n📊 Profile Stats: {stats.count()}")
    for stat in stats:
        print(f"   - Views: {stat.views} | Followers: {stat.followers} | Stars: {stat.stars}")
    
    # Check Projects
    projects = Project.objects.all()
    print(f"\n🚀 Projects: {projects.count()}")
    for project in projects:
        print(f"   - {project.title} ({project.project_type}) - {project.difficulty}")
    
    # Check Skills
    skills = Skill.objects.all()
    print(f"\n💻 Skills: {skills.count()}")
    for skill in skills:
        print(f"   - {skill.name} ({skill.category}) - {skill.proficiency_level}%")
    
    # Check Achievements
    achievements = Achievement.objects.all()
    print(f"\n🏆 Achievements: {achievements.count()}")
    for achievement in achievements:
        print(f"   - {achievement.title} ({achievement.year})")
    
    # Check Education
    education = Education.objects.all()
    print(f"\n🎓 Education: {education.count()}")
    for edu in education:
        print(f"   - {edu.degree} at {edu.institution} ({edu.start_year}-{edu.end_year})")
    
    # Check Experience
    experience = Experience.objects.all()
    print(f"\n💼 Experience: {experience.count()}")
    for exp in experience:
        print(f"   - {exp.title} at {exp.company} ({exp.start_date}-{exp.end_date})")
    
    # Check Certifications
    certifications = Certification.objects.all()
    print(f"\n📜 Certifications: {certifications.count()}")
    for cert in certifications:
        print(f"   - {cert.name} from {cert.issuing_organization}")
    
    # Check Hobbies
    hobbies = Hobby.objects.all()
    print(f"\n🎨 Hobbies: {hobbies.count()}")
    for hobby in hobbies:
        print(f"   - {hobby.name} ({hobby.category})")
    
    print("\n" + "=" * 50)
    
    if projects.count() == 0:
        print("❌ No projects found! Database might be empty.")
        print("💡 Run: python manage.py populate_data")
    else:
        print("✅ Data found! Your portfolio should display content.")
    
    if users.count() == 0:
        print("❌ No users found! Create superuser with:")
        print("💡 python manage.py create_render_superuser --username vijayapardhu --email vijaypardhu17@gmail.com")

if __name__ == '__main__':
    check_data()
