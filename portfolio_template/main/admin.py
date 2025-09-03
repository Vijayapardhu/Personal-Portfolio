from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Project, Achievement, SocialLink, SiteSettings, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'tagline', 'created_at']
    search_fields = ['name', 'email', 'tagline']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'about_text', 'profile_picture')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Documents', {
            'fields': ('resume',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order', 'created_at']
    list_filter = ['category', 'proficiency', 'created_at']
    search_fields = ['name']
    ordering = ['order', 'name']
    list_editable = ['order', 'proficiency']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at', 'tech_stack_display']
    list_filter = ['featured', 'created_at', 'tech_stack']
    search_fields = ['title', 'description']
    ordering = ['order', '-created_at']
    list_editable = ['featured', 'order']
    filter_horizontal = ['tech_stack']
    
    def tech_stack_display(self, obj):
        return ", ".join([skill.name for skill in obj.tech_stack.all()[:3]])
    tech_stack_display.short_description = "Tech Stack"


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
