from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    PROJECT_TYPES = [
        ('android', 'Android App'),
        ('web', 'Web Application'),
        ('desktop', 'Desktop Application'),
        ('api', 'API/Backend'),
        ('ai', 'AI/Automation'),
        ('other', 'Other'),
    ]
    
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, help_text="Brief description for cards")
    technologies = models.JSONField(default=list, help_text="List of technologies used")
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='other')
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, default='intermediate')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    icon = models.CharField(max_length=50, default='fas fa-code', help_text="Font Awesome icon class")
    featured = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    challenges_faced = models.TextField(blank=True, help_text="Technical challenges and how you solved them")
    lessons_learned = models.TextField(blank=True, help_text="Key takeaways from the project")
    impact = models.TextField(blank=True, help_text="Real-world impact or benefits")
    downloads_installs = models.IntegerField(default=0, help_text="Number of downloads/installs if applicable")
    stars = models.IntegerField(default=0, help_text="GitHub stars if applicable")
    forks = models.IntegerField(default=0, help_text="GitHub forks if applicable")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', '-completed_date', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.title
    
    def get_tech_badges(self):
        """Return technologies as formatted badges"""
        return [tech.strip() for tech in self.technologies if tech.strip()]

class Achievement(models.Model):
    """Model for achievements and accomplishments"""
    ACHIEVEMENT_TYPES = [
        ('award', 'Award'),
        ('certification', 'Certification'),
        ('project', 'Project Milestone'),
        ('skill', 'Skill Mastery'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    achievement_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPES, default='other')
    icon = models.CharField(max_length=50, default='🏆', help_text="Emoji or icon name")
    date_achieved = models.DateField(default=timezone.now)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-date_achieved', '-featured']
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    """Model for technical skills"""
    SKILL_CATEGORIES = [
        ('programming', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('tools', 'Tools & IDEs'),
        ('databases', 'Databases'),
        ('cloud', 'Cloud Services'),
        ('design', 'Design Tools'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='programming', blank=False, null=False)
    icon = models.CharField(max_length=50, help_text="Icon name or emoji")
    proficiency = models.IntegerField(default=80, help_text="Skill proficiency percentage (0-100)")
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return self.name

class Hobby(models.Model):
    """Model for hobbies and interests"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default='🎨')
    color = models.CharField(max_length=20, default='blue', help_text="CSS color class")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Hobbies'
    
    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    """Model for contact information"""
    email = models.EmailField()
    github_url = models.URLField()
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Contact Information'
    
    def __str__(self):
        return f"Contact Info - {self.email}"

class ProfileStats(models.Model):
    """Model for profile statistics"""
    profile_views = models.IntegerField(default=0)
    github_followers = models.IntegerField(default=0)
    github_stars = models.IntegerField(default=0)
    projects_count = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Profile Statistics'
    
    def __str__(self):
        return f"Stats - Views: {self.profile_views}, Followers: {self.github_followers}"

class Education(models.Model):
    """Model for educational background"""
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    current = models.BooleanField(default=False)
    score = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-end_year', '-start_year']
        verbose_name_plural = 'Education'
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    """Model for work experience and internships"""
    EXPERIENCE_TYPES = [
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('part-time', 'Part-time'),
        ('volunteer', 'Volunteer'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES, default='internship')
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    technologies_used = models.JSONField(default=list, blank=True)
    achievements = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-start_date', '-end_date']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class Certification(models.Model):
    """Model for certifications and courses"""
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-issue_date', '-featured']
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'
    
    def __str__(self):
        return f"{self.name} from {self.issuing_organization}"
