from django.db import models
from django.urls import reverse


class Course(models.Model):
    slug = models.SlugField("Уникальное название курса",unique=True)
    title = models.CharField("Название курса",max_length=100)
    desc = models.TextField("Описание курса")
    image = models.ImageField("Изображение",default="default.jpg", upload_to="courses_images")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return  reverse("course-page", kwargs={"slug": self.slug})


class Lesson(models.Model):
    slug = models.SlugField('Уникальное название курса',unique=True)
    title = models.CharField(" Название урока", max_length=100)
    desc = models.TextField("Описание урока")
    course = models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name="От какова курса")
    number = models.IntegerField("Номер урока")
    video = models.CharField("Видео юрл", max_length=100,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("lesson-page", kwargs={"slug": self.course.slug, 'lesson_slug': self.slug})



