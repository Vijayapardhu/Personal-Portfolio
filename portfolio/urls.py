from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('download-cv/', views.download_cv, name='download_cv'),
    path('api/projects/', views.api_projects, name='api_projects'),
    path('api/achievements/', views.api_achievements, name='api_achievements'),
    path('api/update-stats/', views.update_stats, name='update_stats'),
]
