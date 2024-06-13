from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('profile/',views.profile_view , name = 'profile' ),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html') , name = 'login' ),
    path('exit/', auth_views.LogoutView.as_view(template_name = "users/exit.html") , name = 'exit' ),
    path('register/', views.register_view , name = 'register' ),

]