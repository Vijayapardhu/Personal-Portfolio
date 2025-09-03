from django.db import models
from django.core.validators import URLValidator


class Profile(models.Model):
    """Profile model for storing personal information"""
    name = models.CharField(max_length=100, help_text="Your full name")
    tagline = models.CharField(max_length=200, help_text="Short professional tagline")
    about_text = models.TextField(help_text="Detailed about me text")
    profile_picture = models.ImageField(upload_to='profile/', help_text="Your profile picture")
    email = models.EmailField(help_text="Your email address")
    phone = models.CharField(max_length=20, blank=True, help_text="Your phone number (optional)")
    location = models.CharField(max_length=100, blank=True, help_text="Your location (optional)")
    resume = models.FileField(upload_to='resume/', blank=True, help_text="Your resume PDF (optional)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Skills model for storing technical skills"""
    SKILL_CATEGORIES = [
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks & Libraries'),
        ('database', 'Databases'),
        ('tool', 'Tools & Platforms'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100, help_text="Skill name")
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='other')
    icon_url = models.URLField(validators=[URLValidator()], help_text="Icon URL from skillicons.dev or FontAwesome")
    proficiency = models.IntegerField(choices=[(i, f"{i}%") for i in range(0, 101, 10)], default=80, help_text="Skill proficiency level")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Project(models.Model):
    """Projects model for storing portfolio projects"""
    title = models.CharField(max_length=200, help_text="Project title")
    description = models.TextField(help_text="Project description")
    short_description = models.CharField(max_length=300, help_text="Short description for cards")
    image = models.ImageField(upload_to='projects/', help_text="Project screenshot or image")
    github_link = models.URLField(blank=True, validators=[URLValidator()], help_text="GitHub repository link")
    live_link = models.URLField(blank=True, validators=[URLValidator()], help_text="Live demo link")
    tech_stack = models.ManyToManyField(Skill, related_name='projects', help_text="Technologies used")
    featured = models.BooleanField(default=False, help_text="Mark as featured project")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Achievement(models.Model):
    """Achievements model for storing accomplishments"""
    title = models.CharField(max_length=200, help_text="Achievement title")
    description = models.TextField(help_text="Achievement description")
    year = models.IntegerField(help_text="Year achieved")
    icon = models.CharField(max_length=50, default="🏆", help_text="Emoji or icon for the achievement")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-year']
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

    def __str__(self):
        return f"{self.title} ({self.year})"


class SocialLink(models.Model):
    """Social media links model"""
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('portfolio', 'Portfolio'),
        ('blog', 'Blog'),
        ('other', 'Other'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, help_text="Social media platform")
    url = models.URLField(validators=[URLValidator()], help_text="Profile URL")
    icon_class = models.CharField(max_length=50, default="fab fa-github", help_text="FontAwesome icon class")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    active = models.BooleanField(default=True, help_text="Show this link on the site")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'platform']
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self):
        return f"{self.get_platform_display()} - {self.url}"


class SiteSettings(models.Model):
    """Site-wide settings for customization"""
    site_name = models.CharField(max_length=100, default="Portfolio", help_text="Site name")
    hero_title = models.CharField(max_length=200, default="Welcome to My Portfolio", help_text="Hero section title")
    hero_subtitle = models.TextField(default="I'm a passionate developer creating amazing digital experiences", help_text="Hero section subtitle")
    primary_color = models.CharField(max_length=7, default="#3B82F6", help_text="Primary theme color (hex)")
    secondary_color = models.CharField(max_length=7, default="#1F2937", help_text="Secondary theme color (hex)")
    accent_color = models.CharField(max_length=7, default="#10B981", help_text="Accent color (hex)")
    enable_dark_mode = models.BooleanField(default=True, help_text="Enable dark/light mode toggle")
    enable_animations = models.BooleanField(default=True, help_text="Enable AOS animations")
    contact_email = models.EmailField(help_text="Email for contact form submissions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return f"Site Settings - {self.site_name}"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            return
        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    """Contact form messages"""
    name = models.CharField(max_length=100, help_text="Sender's name")
    email = models.EmailField(help_text="Sender's email")
    subject = models.CharField(max_length=200, help_text="Message subject")
    message = models.TextField(help_text="Message content")
    read = models.BooleanField(default=False, help_text="Message has been read")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
