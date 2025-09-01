from django.contrib import admin
from .models import Project, Achievement, Skill, Hobby, ContactInfo, ProfileStats, Education, Experience, Certification

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'difficulty_level', 'featured', 'completed_date', 'stars', 'forks']
    list_filter = ['project_type', 'difficulty_level', 'featured', 'completed_date']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured', 'difficulty_level']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'description', 'project_type', 'difficulty_level')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'icon', 'challenges_faced', 'lessons_learned')
        }),
        ('Links & Media', {
            'fields': ('github_url', 'live_url', 'image')
        }),
        ('Metrics & Impact', {
            'fields': ('impact', 'downloads_installs', 'stars', 'forks')
        }),
        ('Settings', {
            'fields': ('featured', 'completed_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'achievement_type', 'date_achieved', 'featured']
    list_filter = ['achievement_type', 'featured', 'date_achieved']
    search_fields = ['title', 'description']
    list_editable = ['featured']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'featured', 'order']
    list_filter = ['category', 'featured']
    search_fields = ['name']
    list_editable = ['proficiency', 'featured', 'order']

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'order']
    search_fields = ['name']
    list_editable = ['color', 'order']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'github_url', 'updated_at']
    readonly_fields = ['updated_at']
    
    def has_add_permission(self, request):
        # Only allow one contact info instance
        return not ContactInfo.objects.exists()

@admin.register(ProfileStats)
class ProfileStatsAdmin(admin.ModelAdmin):
    list_display = ['profile_views', 'github_followers', 'github_stars', 'projects_count', 'updated_at']
    readonly_fields = ['updated_at']
    
    def has_add_permission(self, request):
        # Only allow one stats instance
        return not ProfileStats.objects.exists()

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_year', 'end_year', 'current', 'score']
    list_filter = ['current', 'start_year', 'end_year']
    search_fields = ['degree', 'institution']
    list_editable = ['current', 'score']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'experience_type', 'start_date', 'end_date', 'current']
    list_filter = ['experience_type', 'current', 'start_date', 'end_date']
    search_fields = ['title', 'company', 'description']
    list_editable = ['current']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company', 'experience_type', 'location')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date', 'current')
        }),
        ('Details', {
            'fields': ('description', 'technologies_used', 'achievements')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date', 'expiry_date', 'featured']
    list_filter = ['featured', 'issue_date', 'expiry_date']
    search_fields = ['name', 'issuing_organization', 'description']
    list_editable = ['featured']
    readonly_fields = ['created_at']

# Customize admin site
admin.site.site_header = "Vijaya Pardhu Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
