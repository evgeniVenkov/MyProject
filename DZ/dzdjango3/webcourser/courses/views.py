from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Course, Lesson, Comment
from .forms import CourseForm, CommentForm
from django.contrib.auth.models import User


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
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx


class LessonPage(DetailView):
    model = Course
    template_name = 'courses/lesson_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(LessonPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        less = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

        less.video = less.video.split('embed/')[1]

        ctx['allcoment'] = Comment.objects.filter(lesson=less)

        ctx['Comentform'] = CommentForm
        ctx['title'] = less
        ctx['lesson'] = less
        return ctx

    def post(self, request, *args, **kwargs):

        # course = Course.objects.filter(slug=self.kwargs['slug']).first()
        # lesson = Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).first()

        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

        post = request.POST.copy()
        post['lesson'] = lesson
        post['user'] = request.user
        request.POST = post


        form = CommentForm(post)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        url = self.kwargs['slug'] + '/' + self.kwargs['lesson_slug']
        return redirect('/course/' + url)


class AddCourse(CreateView):
    form_class = CourseForm
    template_name = 'courses/add_course.html'

    # fields = ['slug', 'title', 'desc', 'image']
    def get_context_data(self, **kwargs):
        ctx = super(AddCourse, self).get_context_data(**kwargs)
        ctx['title'] = "Добавить курс"

        return ctx
