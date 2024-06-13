from django.urls import path
from . import views

from django.contrib.auth import views as auth_views





urlpatterns = [
    path('profile/',views.profile_view , name = 'profile' ),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html') , name = 'login' ),
    path('exit/', auth_views.LogoutView.as_view(template_name = "users/exit.html") , name = 'exit' ),
    path('register/', views.register_view , name = 'register' ),

    path('pass-reset/',
         auth_views.PasswordResetView.as_view(template_name = 'users/pass_resert.html'), name='password_reset'),
    path("password_reset_confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path("password_reset_done/",
         auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'),
         name='password_reset_done'),
    path("password_reset_complite/",
         auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_complite.html'),
         name='password_reset_complite'),
]