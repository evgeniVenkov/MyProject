from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile_view , name = 'profile' ),
    path('login/', views.login_view , name = 'login' ),
    path('exit/', views.exit_view , name = 'exit' ),
    path('register/', views.register_view , name = 'register' ),
]