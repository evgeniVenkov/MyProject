from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from .models import Course,Lesson
from .forms import CourseForm


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'
        return ctx


class CoursePage(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    def get_context_data(self, **kwargs):
        ctx = super(CoursePage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug= self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx

class LessonPage(DetailView):
    model = Course
    template_name = 'courses/lesson_detail.html'
    def get_context_data(self, **kwargs):
        ctx = super(LessonPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug = self.kwargs['lesson_slug']).first()

        lesson.video = lesson.video.split('embed/')[1]

        ctx['title'] = lesson
        ctx['lesson'] =lesson
        return ctx

class AddCourse(CreateView):
    form_class = CourseForm
    template_name = 'courses/add_course.html'
    # fields = ['slug', 'title', 'desc', 'image']
    def get_context_data(self, **kwargs):
        ctx = super(AddCourse, self).get_context_data(**kwargs)
        ctx['title'] = "Добавить курс"

        return ctx

