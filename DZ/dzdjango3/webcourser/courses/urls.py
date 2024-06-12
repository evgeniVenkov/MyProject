from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('course/<slug>/', views.CoursePage.as_view(), name='course-page'),
    path('course/<slug>/<lesson_slug>/', views.LessonPage.as_view(), name='lesson-page'),
    path('add-course/', views.AddCourse.as_view(), name='add-course'),
]