from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from ..users import views as users_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('blog.urls')),
    path('register', include('users.urls')),
    path('profile', include('users.urls')),
    path('user', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('exit/', auth_views.LogoutView.as_view(template_name='users/exit.html'), name='exit'),

]
