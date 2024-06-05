from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователся', default='user_img/default.png', upload_to='user_img')

    def __str__(self):
        return f'Профиль Пользователя: {self.user.username}'


    def save(self,*args, **kwargs):
        super().save()
        img = Image.open(self.img.path)

        if img.height > 256 or img.width > 256:
            resize = (256, 256)
            img.thumbnail(resize)
            img.save(self.img.path)
    class Meta:
        verbose_name = "Штуку профиля"
        verbose_name_plural = "Штуки профиля"

# Create your models here.
