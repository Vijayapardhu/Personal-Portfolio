from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Profile, Skill, Project, Achievement, SocialLink, SiteSettings, ContactMessage
from .forms import ContactForm


def get_common_context():
    """Get common context data for all pages"""
    try:
        profile = Profile.objects.first()
        skills = Skill.objects.all()
        projects = Project.objects.all()
        achievements = Achievement.objects.all()
        social_links = SocialLink.objects.filter(active=True)
        site_settings = SiteSettings.objects.first()
        
        # Create default site settings if none exist
        if not site_settings:
            site_settings = SiteSettings.objects.create(
                site_name="Portfolio",
                hero_title="Welcome to My Portfolio",
                hero_subtitle="I'm a passionate developer creating amazing digital experiences",
                contact_email="your-email@example.com"
            )
        
        return {
            'profile': profile,
            'skills': skills,
            'projects': projects,
            'achievements': achievements,
            'social_links': social_links,
            'site_settings': site_settings,
        }
    except Exception as e:
        # Return empty context if there's an error
        return {
            'profile': None,
            'skills': [],
            'projects': [],
            'achievements': [],
            'social_links': [],
            'site_settings': None,
        }


def home(request):
    """Home page view"""
    context = get_common_context()
    
    # Get featured projects
    if context['projects']:
        featured_projects = context['projects'].filter(featured=True)[:3]
        context['featured_projects'] = featured_projects
    
    return render(request, 'main/home.html', context)


def about(request):
    """About page view"""
    context = get_common_context()
    
    # Group skills by category
    if context['skills']:
        skills_by_category = {}
        for skill in context['skills']:
            if skill.category not in skills_by_category:
                skills_by_category[skill.category] = []
            skills_by_category[skill.category].append(skill)
        context['skills_by_category'] = skills_by_category
    
    return render(request, 'main/about.html', context)


def projects(request):
    """Projects page view"""
    context = get_common_context()
    
    # Get featured projects
    if context['projects']:
        featured_projects = context['projects'].filter(featured=True)[:3]
        context['featured_projects'] = featured_projects
    
    return render(request, 'main/projects.html', context)


def contact(request):
    """Contact page view"""
    context = get_common_context()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send email notification
            try:
                if context['site_settings'] and context['site_settings'].contact_email:
                    send_mail(
                        subject=f"New Contact Message: {contact_message.subject}",
                        message=f"""
                        New message from your portfolio website:
                        
                        Name: {contact_message.name}
                        Email: {contact_message.email}
                        Subject: {contact_message.subject}
                        Message: {contact_message.message}
                        """,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[context['site_settings'].contact_email],
                        fail_silently=True,
                    )
            except Exception as e:
                # Log error but don't break the form submission
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context['form'] = form
    return render(request, 'main/contact.html', context)


def project_detail(request, project_id):
    """Project detail page view"""
    context = get_common_context()
    
    try:
        project = Project.objects.get(id=project_id)
        context['project'] = project
    except Project.DoesNotExist:
        messages.error(request, 'Project not found.')
        return redirect('projects')
    
    return render(request, 'main/project_detail.html', context)


def skills(request):
    """Skills page view"""
    context = get_common_context()
    
    # Group skills by category
    if context['skills']:
        skills_by_category = {}
        for skill in context['skills']:
            if skill.category not in skills_by_category:
                skills_by_category[skill.category] = []
            skills_by_category[skill.category].append(skill)
        context['skills_by_category'] = skills_by_category
        
        # Get highest proficiency
        highest_proficiency = max(skill.proficiency for skill in context['skills'])
        context['highest_proficiency'] = highest_proficiency
    
    return render(request, 'main/skills.html', context)


def achievements(request):
    """Achievements page view"""
    context = get_common_context()
    return render(request, 'main/achievements.html', context)


def download_resume(request):
    """Download resume view"""
    context = get_common_context()
    
    if context['profile'] and context['profile'].resume:
        return redirect(context['profile'].resume.url)
    
    messages.error(request, 'Resume not available.')
    return redirect('about')
