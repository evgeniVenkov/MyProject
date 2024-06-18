from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html') , name = 'login' ),
    path('profile/', views.profile_view, name='profile'),
]
