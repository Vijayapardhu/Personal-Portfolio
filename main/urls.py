from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('skills/', views.skills, name='skills'),
    path('achievements/', views.achievements, name='achievements'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.download_resume, name='download_resume'),
]
