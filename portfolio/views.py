from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q
from .models import Project, Achievement, Skill, Hobby, ContactInfo, ProfileStats, Education, Experience, Certification
import json
import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from io import BytesIO

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
        education = Education.objects.all()  # Get all education records
        experience = Experience.objects.all()[:3]
        certifications = Certification.objects.all()[:3]

        # Debug logging
        print(f"DEBUG: Found {projects.count()} projects")
        print(f"DEBUG: Found {achievements.count()} achievements")
        print(f"DEBUG: Found {skills.count()} skills")
        print(f"DEBUG: Found {hobbies.count()} hobbies")
        print(f"DEBUG: Found {education.count()} education records")

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
        
        # Debug logging
        print(f"DEBUG: Found {projects.count()} projects")
        
        context = {
            'projects': projects,
        }
        
        return render(request, 'portfolio/projects.html', context)
        
    except Exception as e:
        print(f"ERROR in projects view: {str(e)}")
        return HttpResponse(f"Error loading projects page: {str(e)}")

def about(request):
    """About page view with detailed portfolio information"""
    try:
        # Get all the data
        education = Education.objects.all()  # Get all education records
        skills = Skill.objects.all()
        experience = Experience.objects.all()
        certifications = Certification.objects.all()
        hobbies = Hobby.objects.all()
        contact_info = ContactInfo.objects.first()

        # Debug logging
        print(f"DEBUG: Found {education.count()} education records")
        print(f"DEBUG: Found {skills.count()} skills")
        print(f"DEBUG: Found {experience.count()} experience records")
        print(f"DEBUG: Found {certifications.count()} certifications")

        context = {
            'education': education,
            'skills': skills,
            'experience': experience,
            'certifications': certifications,
            'hobbies': hobbies,
            'contact_info': contact_info,
        }

        return render(request, 'portfolio/about.html', context)

    except Exception as e:
        print(f"ERROR in about view: {str(e)}")
        return HttpResponse(f"Error loading about page: {str(e)}")

def contact(request):
    """Contact page view"""
    try:
        contact_info = ContactInfo.objects.first()
        
        # Debug logging
        print(f"DEBUG: Contact info: {contact_info}")
        
        context = {
            'contact_info': contact_info,
        }
        
        return render(request, 'portfolio/contact.html', context)
        
    except Exception as e:
        print(f"ERROR in contact view: {str(e)}")
        return HttpResponse(f"Error loading contact page: {str(e)}")

def download_cv(request):
    """Generate and download CV as PDF"""
    try:
        # Get all portfolio data
        education = Education.objects.all().order_by('-end_year', '-start_year')
        skills = Skill.objects.all().order_by('category', 'order')
        projects = Project.objects.filter(featured=True).order_by('-created_at')
        achievements = Achievement.objects.filter(featured=True).order_by('-date_achieved')
        
        # Create PDF
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        story = []
        
        # Styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=colors.darkblue
        )
        
        normal_style = styles['Normal']
        
        # Header
        story.append(Paragraph("VIJAYA PARDHU", title_style))
        story.append(Paragraph("Student | Android & Web Developer | Firebase Enthusiast", 
                              ParagraphStyle('Subtitle', parent=styles['Normal'], alignment=TA_CENTER, fontSize=14)))
        story.append(Spacer(1, 20))
        
        # Contact Info
        contact_info = ContactInfo.objects.first()
        if contact_info:
            contact_data = [
                ['Email:', contact_info.email],
                ['GitHub:', contact_info.github_url],
            ]
            if contact_info.phone:
                contact_data.append(['Phone:', contact_info.phone])
            if contact_info.location:
                contact_data.append(['Location:', contact_info.location])
            
            contact_table = Table(contact_data, colWidths=[1.5*inch, 4*inch])
            contact_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            story.append(Paragraph("Contact Information", heading_style))
            story.append(contact_table)
            story.append(Spacer(1, 20))
        
        # Education
        if education:
            story.append(Paragraph("Education", heading_style))
            for edu in education:
                edu_text = f"<b>{edu.degree}</b><br/>"
                edu_text += f"{edu.institution}"
                if edu.location:
                    edu_text += f", {edu.location}"
                edu_text += f"<br/>"
                if edu.current:
                    edu_text += f"{edu.start_year} - Present"
                else:
                    edu_text += f"{edu.start_year} - {edu.end_year}"
                if edu.score:
                    edu_text += f" | Score: {edu.score}"
                if edu.description:
                    edu_text += f"<br/>{edu.description}"
                
                story.append(Paragraph(edu_text, normal_style))
                story.append(Spacer(1, 12))
        
        # Skills
        if skills:
            story.append(Paragraph("Technical Skills", heading_style))
            skill_categories = {}
            for skill in skills:
                if skill.category not in skill_categories:
                    skill_categories[skill.category] = []
                skill_categories[skill.category].append(skill)
            
            for category, category_skills in skill_categories.items():
                category_name = dict(Skill.SKILL_CATEGORIES)[category]
                story.append(Paragraph(f"<b>{category_name}</b>", normal_style))
                skill_text = ", ".join([f"{skill.name} ({skill.proficiency_level}%)" for skill in category_skills])
                story.append(Paragraph(skill_text, normal_style))
                story.append(Spacer(1, 8))
        
        # Projects
        if projects:
            story.append(Paragraph("Featured Projects", heading_style))
            for project in projects:
                project_text = f"<b>{project.title}</b><br/>"
                project_text += f"{project.description}<br/>"
                if project.technologies:
                    project_text += f"Technologies: {', '.join(project.technologies)}<br/>"
                if project.github_url:
                    project_text += f"GitHub: {project.github_url}"
                
                story.append(Paragraph(project_text, normal_style))
                story.append(Spacer(1, 12))
        
        # Achievements
        if achievements:
            story.append(Paragraph("Achievements", heading_style))
            for achievement in achievements:
                achievement_text = f"<b>{achievement.title}</b><br/>"
                achievement_text += f"{achievement.description}<br/>"
                achievement_text += f"Achieved: {achievement.date_achieved.strftime('%B %Y')}"
                
                story.append(Paragraph(achievement_text, normal_style))
                story.append(Spacer(1, 12))
        
        # Goal
        story.append(Paragraph("Career Goal", heading_style))
        goal_text = "To become a Full-Stack Developer, skilled in Android, Cloud, and Modern Web Tech, while contributing to open-source & building meaningful tech for society."
        story.append(Paragraph(goal_text, normal_style))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        
        # Create response
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Vijaya_Pardhu_CV_{datetime.now().strftime("%Y%m%d")}.pdf"'
        
        return response
        
    except Exception as e:
        print(f"ERROR in download_cv: {str(e)}")
        return HttpResponse(f"Error generating CV: {str(e)}")

@csrf_exempt
def update_stats(request):
    """Update profile statistics (for GitHub integration)"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            stats, created = ProfileStats.objects.get_or_create(id=1)
            
            if 'followers' in data:
                stats.github_followers = data['followers']
            if 'stars' in data:
                stats.github_stars = data['stars']
            if 'projects' in data:
                stats.projects_count = data['projects']
            
            stats.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

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
            'education_count': Education.objects.count(),
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

        if Education.objects.exists():
            data['sample_education'] = {
                'degree': Education.objects.first().degree,
                'institution': Education.objects.first().institution
            }

        return JsonResponse(data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
