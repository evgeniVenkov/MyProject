from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('profile/',views.profile_view , name = 'profile' ),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html') , name = 'login' ),
    path('exit/', auth_views.LogoutView.as_view(template_name = "users/exit.html") , name = 'exit' ),
    path('register/', views.register_view , name = 'register' ),
    path('posts/',views.ShowPosts.as_view() , name = 'posts' ),
    path('posts/<int:pk>',views.DetailPosts.as_view() , name = 'post-deteil' ),
    path('post/add', views.CreatePosts.as_view(), name = 'post-add' ),
    path('post/<int:pk>/update',views.UpdatePosts.as_view() , name = 'post-update' ),
    path('post/<int:pk>/delete',views.DeletePost.as_view() , name = 'post-delete' ),
    path('post/<str:username>',views.ShowPostsUser.as_view() , name = 'post-user' ),
    path('contakti/',views.Pochta.as_view(),name='pochta'),

]