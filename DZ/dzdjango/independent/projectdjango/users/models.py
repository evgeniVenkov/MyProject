from django.db import models
from django.contrib.auth.models import User


class Profole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователся', default='default.png', upload_to='user_img')

    def __str__(self):
        return f'Профиль Пользователя: {self.user.username}'


# Create your models here.
