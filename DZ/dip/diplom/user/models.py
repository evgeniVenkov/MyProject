from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'Профиль Пользователя: {self.user.username}'

class links(models.Model):
    link = models.CharField(max_length=250)
    slug = models.SlugField(max_length=120,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.slug
# Create your models here.
