from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    #path('request/', views.ContactView.as_view() , name='request'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('branch/', views.branch, name='branch'),
    path('events/', views.events, name='events'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('about-details/<str:ID>/', views.aboutDetails, name='about-details'),
    path('branch-details/<str:ID>/', views.branchDetails, name='branch-details'),
    path('project-details/<str:ID>/', views.projectDetails, name='project-details'),
    path('events-details/<str:ID>/', views.eventsDetails, name='events-details'),
    #path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    #path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]