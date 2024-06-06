from django.db import models
from django.contrib.auth.models import User
from PIL import Image

choise = (('male','Мужской'),('female','Женский'))

class Profile(models.Model):
    soglasie = models.BooleanField(default=False)
    pol = models.CharField('Выбирите пол', max_length=6, choices=choise,default='male')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField("Фото Пользователя" ,default = 'user_img/default.png', upload_to='user_img')

    def __str__(self):
        return f'Профиль Пользователя: {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.img.path)

        if img.height > 300 or img.width > 300:
            resize = (300,300)
            img.thumbnail(resize)
            img.save(self.img.path)


