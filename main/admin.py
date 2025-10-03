from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Project, Achievement, SocialLink, SiteSettings, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'tagline', 'created_at']
    search_fields = ['name', 'email', 'tagline', 'about_text']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['tagline']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'about_text', 'profile_picture'),
            'description': 'Basic profile information that appears on your portfolio'
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location'),
            'description': 'Contact details displayed on your contact page'
        }),
        ('Documents', {
            'fields': ('resume',),
            'description': 'Upload your resume for download'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one profile instance
        return not Profile.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of profile
        return False


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order', 'icon_preview', 'created_at']
    list_filter = ['category', 'proficiency', 'created_at']
    search_fields = ['name', 'category']
    ordering = ['order', 'name']
    list_editable = ['order', 'proficiency', 'category']
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'proficiency'),
            'description': 'Basic skill information'
        }),
        ('Display Settings', {
            'fields': ('icon_url', 'order'),
            'description': 'How the skill appears on your portfolio'
        }),
    )
    
    def icon_preview(self, obj):
        if obj.icon_url:
            return format_html('<img src="{}" width="24" height="24" style="border-radius: 4px;" />', obj.icon_url)
        return "No icon"
    icon_preview.short_description = "Icon"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'image_preview', 'tech_stack_display', 'created_at']
    list_filter = ['featured', 'created_at', 'tech_stack']
    search_fields = ['title', 'description', 'short_description']
    ordering = ['order', '-created_at']
    list_editable = ['featured', 'order']
    filter_horizontal = ['tech_stack']
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'short_description', 'image'),
            'description': 'Basic project information and description'
        }),
        ('Links', {
            'fields': ('github_link', 'live_link'),
            'description': 'Project links (GitHub repository and live demo)'
        }),
        ('Technology & Display', {
            'fields': ('tech_stack', 'featured', 'order'),
            'description': 'Technologies used and display settings'
        }),
    )
    
    def tech_stack_display(self, obj):
        return ", ".join([skill.name for skill in obj.tech_stack.all()[:3]])
    tech_stack_display.short_description = "Tech Stack"
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="30" style="object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "No image"
    image_preview.short_description = "Preview"


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'icon', 'order', 'created_at']
    list_filter = ['year', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['order', '-year']
    list_editable = ['year', 'icon', 'order']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'active', 'order', 'created_at']
    list_filter = ['platform', 'active', 'created_at']
    search_fields = ['platform', 'url']
    ordering = ['order', 'platform']
    list_editable = ['active', 'order']


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'contact_email', 'enable_dark_mode', 'enable_animations', 'updated_at']
    list_editable = ['enable_dark_mode', 'enable_animations']
    
    fieldsets = (
        ('Site Information', {
            'fields': ('site_name', 'hero_title', 'hero_subtitle'),
            'description': 'Basic site information and hero section content'
        }),
        ('Theme Colors', {
            'fields': ('primary_color', 'secondary_color', 'accent_color'),
            'description': 'Customize your site colors (use hex codes like #3B82F6)'
        }),
        ('Features', {
            'fields': ('enable_dark_mode', 'enable_animations'),
            'description': 'Enable or disable site features'
        }),
        ('Contact', {
            'fields': ('contact_email',),
            'description': 'Email address for contact form submissions'
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of site settings
        return False


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'read', 'created_at']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    list_editable = ['read']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        # Don't allow manual creation of contact messages
        return False
    
    def has_change_permission(self, request, obj=None):
        # Only allow marking as read
        return True
    
    def has_delete_permission(self, request, obj=None):
        # Allow deletion of old messages
        return True


# Customize admin site
admin.site.site_header = "Portfolio Template Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Template Administration"
