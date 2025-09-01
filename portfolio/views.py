from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO
from .models import Project, Achievement, Skill, Hobby, ContactInfo, ProfileStats, Education, Experience, Certification
import json

def home(request):
    """Home page view with comprehensive portfolio data"""
    context = {
        'profile_stats': ProfileStats.objects.first(),
        'education': Education.objects.filter(current=True).first(),
        'featured_projects': Project.objects.filter(featured=True)[:6],
        'skills': Skill.objects.filter(featured=True).order_by('category', 'order')[:12],
        'achievements': Achievement.objects.filter(featured=True)[:6],
        'hobbies': Hobby.objects.all().order_by('order')[:6],
        'experience': Experience.objects.filter(current=True)[:3],
        'certifications': Certification.objects.filter(featured=True)[:4],
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """About page view with detailed information"""
    context = {
        'education': Education.objects.all().order_by('-end_year', '-start_year'),
        'skills': Skill.objects.all().order_by('category', 'order'),
        'achievements': Achievement.objects.all().order_by('-date_achieved', '-featured'),
        'experience': Experience.objects.all().order_by('-start_date', '-end_date'),
        'certifications': Certification.objects.all().order_by('-issue_date', '-featured'),
        'hobbies': Hobby.objects.all().order_by('order'),
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    """Projects page view with all projects"""
    context = {
        'projects': Project.objects.all().order_by('-featured', '-completed_date', '-created_at'),
        'project_types': Project.PROJECT_TYPES,
        'difficulty_levels': Project.DIFFICULTY_LEVELS,
    }
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    """Contact page view"""
    context = {
        'contact_info': ContactInfo.objects.first(),
        'profile_stats': ProfileStats.objects.first(),
    }
    return render(request, 'portfolio/contact.html', context)

def download_cv(request):
    """Generate and download CV as PDF"""
    # Get all the data needed for CV
    contact_info = ContactInfo.objects.first()
    education = Education.objects.all().order_by('-end_year', '-start_year')
    skills = Skill.objects.all().order_by('category', 'order')
    experience = Experience.objects.all().order_by('-start_date', '-end_date')
    projects = Project.objects.filter(featured=True).order_by('-completed_date')
    achievements = Achievement.objects.filter(featured=True).order_by('-date_achieved')
    certifications = Certification.objects.filter(featured=True).order_by('-issue_date')
    
    # Create the PDF
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
        alignment=1,  # Center
        textColor=colors.HexColor('#3B82F6')
    )
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.HexColor('#1F2937')
    )
    normal_style = styles['Normal']
    
    # Title
    story.append(Paragraph("VIJAYA PARDHU", title_style))
    story.append(Paragraph("Student | Android & Web Developer | Firebase Enthusiast", styles['Heading3']))
    story.append(Spacer(1, 20))
    
    # Contact Information
    if contact_info:
        story.append(Paragraph("CONTACT INFORMATION", heading_style))
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
        story.append(contact_table)
        story.append(Spacer(1, 20))
    
    # Education
    if education:
        story.append(Paragraph("EDUCATION", heading_style))
        for edu in education:
            edu_text = f"<b>{edu.degree}</b><br/>"
            edu_text += f"{edu.institution}"
            if edu.location:
                edu_text += f", {edu.location}"
            edu_text += f"<br/>{edu.start_year}"
            if edu.current:
                edu_text += " - Present"
            elif edu.end_year:
                edu_text += f" - {edu.end_year}"
            if edu.score:
                edu_text += f" | Score: {edu.score}"
            story.append(Paragraph(edu_text, normal_style))
            story.append(Spacer(1, 12))
        story.append(Spacer(1, 20))
    
    # Skills
    if skills:
        story.append(Paragraph("TECHNICAL SKILLS", heading_style))
        skill_categories = {}
        for skill in skills:
            if skill.category not in skill_categories:
                skill_categories[skill.category] = []
            skill_categories[skill.category].append(skill)
        
        for category, category_skills in skill_categories.items():
            category_name = dict(Skill.SKILL_CATEGORIES)[category]
            story.append(Paragraph(f"<b>{category_name}:</b>", normal_style))
            skill_names = [skill.name for skill in category_skills]
            story.append(Paragraph(", ".join(skill_names), normal_style))
            story.append(Spacer(1, 8))
        story.append(Spacer(1, 20))
    
    # Experience
    if experience:
        story.append(Paragraph("EXPERIENCE", heading_style))
        for exp in experience:
            exp_text = f"<b>{exp.title}</b> at <b>{exp.company}</b><br/>"
            exp_text += f"{exp.start_date.strftime('%B %Y')}"
            if exp.current:
                exp_text += " - Present"
            elif exp.end_date:
                exp_text += f" - {exp.end_date.strftime('%B %Y')}"
            if exp.location:
                exp_text += f" | {exp.location}"
            exp_text += f"<br/>{exp.description}"
            story.append(Paragraph(exp_text, normal_style))
            story.append(Spacer(1, 12))
        story.append(Spacer(1, 20))
    
    # Featured Projects
    if projects:
        story.append(Paragraph("FEATURED PROJECTS", heading_style))
        for project in projects:
            proj_text = f"<b>{project.title}</b><br/>"
            proj_text += f"{project.short_description}<br/>"
            proj_text += f"<b>Technologies:</b> {', '.join(project.technologies[:5])}<br/>"
            proj_text += f"<b>Type:</b> {dict(Project.PROJECT_TYPES)[project.project_type]} | "
            proj_text += f"<b>Difficulty:</b> {dict(Project.DIFFICULTY_LEVELS)[project.difficulty_level]}"
            if project.completed_date:
                proj_text += f" | <b>Completed:</b> {project.completed_date.strftime('%B %Y')}"
            story.append(Paragraph(proj_text, normal_style))
            story.append(Spacer(1, 12))
        story.append(Spacer(1, 20))
    
    # Achievements
    if achievements:
        story.append(Paragraph("ACHIEVEMENTS", heading_style))
        for achievement in achievements:
            ach_text = f"<b>{achievement.title}</b><br/>"
            ach_text += f"{achievement.description}<br/>"
            ach_text += f"<b>Type:</b> {dict(Achievement.ACHIEVEMENT_TYPES)[achievement.achievement_type]} | "
            ach_text += f"<b>Date:</b> {achievement.date_achieved.strftime('%B %Y')}"
            story.append(Paragraph(ach_text, normal_style))
            story.append(Spacer(1, 12))
        story.append(Spacer(1, 20))
    
    # Certifications
    if certifications:
        story.append(Paragraph("CERTIFICATIONS", heading_style))
        for cert in certifications:
            cert_text = f"<b>{cert.name}</b> from <b>{cert.issuing_organization}</b><br/>"
            cert_text += f"Issued: {cert.issue_date.strftime('%B %Y')}"
            if cert.expiry_date:
                cert_text += f" | Expires: {cert.expiry_date.strftime('%B %Y')}"
            if cert.description:
                cert_text += f"<br/>{cert.description}"
            story.append(Paragraph(cert_text, normal_style))
            story.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    
    # Create response
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Vijaya_Pardhu_CV.pdf"'
    return response

@csrf_exempt
def update_stats(request):
    """Update profile statistics (simulated GitHub stats)"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            stats, created = ProfileStats.objects.get_or_create(
                profile_views=0,
                defaults={
                    'github_followers': 25,
                    'github_stars': 15,
                    'projects_count': 8
                }
            )
            
            if 'github_followers' in data:
                stats.github_followers = data['github_followers']
            if 'github_stars' in data:
                stats.github_stars = data['github_stars']
            if 'projects_count' in data:
                stats.projects_count = data['projects_count']
            
            stats.save()
            return JsonResponse({'status': 'success', 'message': 'Stats updated successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)

def api_projects(request):
    """API endpoint for projects data"""
    projects = Project.objects.all().order_by('-featured', '-completed_date', '-created_at')
    projects_data = []
    
    for project in projects:
        projects_data.append({
            'id': project.id,
            'title': project.title,
            'short_description': project.short_description,
            'description': project.description,
            'technologies': project.technologies,
            'project_type': project.project_type,
            'difficulty_level': project.difficulty_level,
            'github_url': project.github_url,
            'live_url': project.live_url,
            'icon': project.icon,
            'featured': project.featured,
            'completed_date': project.completed_date.isoformat() if project.completed_date else None,
            'challenges_faced': project.challenges_faced,
            'lessons_learned': project.lessons_learned,
            'impact': project.impact,
            'downloads_installs': project.downloads_installs,
            'stars': project.stars,
            'forks': project.forks,
            'created_at': project.created_at.isoformat(),
            'updated_at': project.updated_at.isoformat(),
        })
    
    return JsonResponse({'projects': projects_data})

def api_achievements(request):
    """API endpoint for achievements data"""
    achievements = Achievement.objects.all().order_by('-date_achieved', '-featured')
    achievements_data = []
    
    for achievement in achievements:
        achievements_data.append({
            'id': achievement.id,
            'title': achievement.title,
            'description': achievement.description,
            'achievement_type': achievement.achievement_type,
            'icon': achievement.icon,
            'date_achieved': achievement.date_achieved.isoformat(),
            'featured': achievement.featured,
            'created_at': achievement.created_at.isoformat(),
        })
    
    return JsonResponse({'achievements': achievements_data})
