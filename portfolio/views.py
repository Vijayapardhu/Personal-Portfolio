from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q
from .models import Project, Achievement, Skill, Hobby, ContactInfo, ProfileStats, Education, Experience, Certification
import json
import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from io import BytesIO
from datetime import datetime

def home(request):
    """Home page view with portfolio data"""
    try:
        # Get all the data
        projects = Project.objects.all()[:3]  # Featured projects
        achievements = Achievement.objects.all()[:6]
        skills = Skill.objects.all()
        hobbies = Hobby.objects.all()
        contact_info = ContactInfo.objects.first()
        profile_stats = ProfileStats.objects.first()
        education = Education.objects.first()
        experience = Experience.objects.all()[:3]
        certifications = Certification.objects.all()[:3]
        
        # Debug logging
        print(f"DEBUG: Found {projects.count()} projects")
        print(f"DEBUG: Found {achievements.count()} achievements")
        print(f"DEBUG: Found {skills.count()} skills")
        print(f"DEBUG: Found {hobbies.count()} hobbies")
        
        context = {
            'projects': projects,
            'achievements': achievements,
            'skills': skills,
            'hobbies': hobbies,
            'contact_info': contact_info,
            'profile_stats': profile_stats,
            'education': education,
            'experience': experience,
            'certifications': certifications,
        }
        
        return render(request, 'portfolio/home.html', context)
        
    except Exception as e:
        print(f"ERROR in home view: {str(e)}")
        # Return a simple response if there's an error
        return HttpResponse(f"Error loading portfolio: {str(e)}")

def projects(request):
    """Projects page view"""
    try:
        projects = Project.objects.all()
        project_types = Project.objects.values_list('project_type', flat=True).distinct()
        
        # Debug logging
        print(f"DEBUG: Found {projects.count()} projects")
        
        context = {
            'projects': projects,
            'project_types': project_types,
        }
        
        return render(request, 'portfolio/projects.html', context)
        
    except Exception as e:
        print(f"ERROR in projects view: {str(e)}")
        return HttpResponse(f"Error loading projects page: {str(e)}")

def about(request):
    """About page view"""
    try:
        education = Education.objects.first()
        skills = Skill.objects.all()
        experience = Experience.objects.all()
        certifications = Certification.objects.all()
        hobbies = Hobby.objects.all()
        
        # Debug logging
        print(f"DEBUG: Found {skills.count()} skills")
        print(f"DEBUG: Found {experience.count()} experience entries")
        print(f"DEBUG: Found {certifications.count()} certifications")
        
        context = {
            'education': education,
            'skills': skills,
            'experience': experience,
            'certifications': certifications,
            'hobbies': hobbies,
        }
        
        return render(request, 'portfolio/about.html', context)
        
    except Exception as e:
        print(f"ERROR in about view: {str(e)}")
        return HttpResponse(f"Error loading about page: {str(e)}")

def contact(request):
    """Contact page view"""
    try:
        contact_info = ContactInfo.objects.first()
        profile_stats = ProfileStats.objects.first()
        
        # Debug logging
        print(f"DEBUG: Contact info: {contact_info}")
        print(f"DEBUG: Profile stats: {profile_stats}")
        
        context = {
            'contact_info': contact_info,
            'profile_stats': profile_stats,
        }
        
        return render(request, 'portfolio/contact.html', context)
        
    except Exception as e:
        print(f"ERROR in contact view: {str(e)}")
        return HttpResponse(f"Error loading contact page: {str(e)}")

def download_cv(request):
    """Download CV as PDF"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.units import inch
        from io import BytesIO
        
        # Get portfolio data
        contact_info = ContactInfo.objects.first()
        education = Education.objects.first()
        skills = Skill.objects.all()
        experience = Experience.objects.all()
        certifications = Certification.objects.all()
        
        # Create PDF
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=getSampleStyleSheet()['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1
        )
        story.append(Paragraph("Vijaya Pardhu - Portfolio", title_style))
        story.append(Spacer(1, 20))
        
        # Contact Info
        if contact_info:
            story.append(Paragraph(f"Email: {contact_info.email}", getSampleStyleSheet()['Normal']))
            story.append(Paragraph(f"GitHub: {contact_info.github_username}", getSampleStyleSheet()['Normal']))
            story.append(Paragraph(f"Location: {contact_info.location}", getSampleStyleSheet()['Normal']))
            story.append(Spacer(1, 20))
        
        # Education
        if education:
            story.append(Paragraph("Education", getSampleStyleSheet()['Heading2']))
            story.append(Paragraph(f"{education.degree} at {education.institution}", getSampleStyleSheet()['Normal']))
            story.append(Paragraph(f"Period: {education.start_year} - {education.end_year}", getSampleStyleSheet()['Normal']))
            story.append(Paragraph(f"Score: {education.score}%", getSampleStyleSheet()['Normal']))
            story.append(Spacer(1, 20))
        
        # Skills
        if skills.exists():
            story.append(Paragraph("Technical Skills", getSampleStyleSheet()['Heading2']))
            for skill in skills:
                story.append(Paragraph(f"• {skill.name} ({skill.proficiency_level}%)", getSampleStyleSheet()['Normal']))
            story.append(Spacer(1, 20))
        
        # Experience
        if experience.exists():
            story.append(Paragraph("Experience", getSampleStyleSheet()['Heading2']))
            for exp in experience:
                story.append(Paragraph(f"• {exp.title} at {exp.company}", getSampleStyleSheet()['Normal']))
                story.append(Paragraph(f"  {exp.start_date} - {exp.end_date}", getSampleStyleSheet()['Normal']))
                story.append(Paragraph(f"  {exp.description}", getSampleStyleSheet()['Normal']))
                story.append(Spacer(1, 10))
            story.append(Spacer(1, 20))
        
        # Certifications
        if certifications.exists():
            story.append(Paragraph("Certifications", getSampleStyleSheet()['Heading2']))
            for cert in certifications:
                story.append(Paragraph(f"• {cert.name} from {cert.issuing_organization}", getSampleStyleSheet()['Normal']))
                story.append(Paragraph(f"  Issued: {cert.issue_date}", getSampleStyleSheet()['Normal']))
                story.append(Spacer(1, 10))
        
        doc.build(story)
        buffer.seek(0)
        
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Vijaya_Pardhu_Portfolio.pdf"'
        return response
        
    except Exception as e:
        print(f"ERROR in download_cv: {str(e)}")
        return HttpResponse(f"Error generating CV: {str(e)}")

@csrf_exempt
def update_stats(request):
    """Update profile stats (simulated)"""
    try:
        profile_stats = ProfileStats.objects.first()
        if profile_stats:
            # Simulate stats update
            profile_stats.views += 1
            profile_stats.save()
            return JsonResponse({'success': True, 'views': profile_stats.views})
        return JsonResponse({'success': False, 'error': 'No profile stats found'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def api_projects(request):
    """API endpoint for projects"""
    try:
        projects = Project.objects.all()
        data = []
        for project in projects:
            data.append({
                'id': project.id,
                'title': project.title,
                'description': project.description,
                'project_type': project.project_type,
                'difficulty': project.difficulty,
                'github_url': project.github_url,
                'live_url': project.live_url,
                'technologies': project.technologies,
                'completion_date': project.completion_date.strftime('%Y-%m-%d') if project.completion_date else None,
                'github_stars': project.github_stars,
                'github_forks': project.github_forks,
            })
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def api_achievements(request):
    """API endpoint for achievements"""
    try:
        achievements = Achievement.objects.all()
        data = []
        for achievement in achievements:
            data.append({
                'id': achievement.id,
                'title': achievement.title,
                'description': achievement.description,
                'year': achievement.year,
                'icon': achievement.icon,
            })
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def debug_data(request):
    """Debug view to check what data is available"""
    try:
        data = {
            'projects_count': Project.objects.count(),
            'achievements_count': Achievement.objects.count(),
            'skills_count': Skill.objects.count(),
            'hobbies_count': Hobby.objects.count(),
            'contact_info_exists': ContactInfo.objects.exists(),
            'profile_stats_exists': ProfileStats.objects.exists(),
            'education_exists': Education.objects.exists(),
            'experience_count': Experience.objects.count(),
            'certifications_count': Certification.objects.count(),
        }
        
        # Get sample data
        if Project.objects.exists():
            data['sample_project'] = {
                'title': Project.objects.first().title,
                'description': Project.objects.first().description[:100] + '...' if len(Project.objects.first().description) > 100 else Project.objects.first().description
            }
        
        if Skill.objects.exists():
            data['sample_skills'] = list(Skill.objects.values('name', 'proficiency_level')[:5])
        
        return JsonResponse(data)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
