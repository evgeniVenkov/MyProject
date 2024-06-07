from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse


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

class Pochta(models.Model):
    tema = models.CharField('Тема письма', max_length=50)
    mail = models.CharField("Почта отправителя" , max_length=50)
    text = models.TextField("Текст сообщения")
    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
    def get_absolute_url(self):
        return reverse('main')
    def __str__(self):
        return f'{self.tema}'

class Posts(models.Model):
    title = models.CharField('Название стратьи',unique= True,max_length=100)
    content = models.TextField('основной текст')
    avtor = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Автор")
    date = models.DateTimeField('Дата' ,default=timezone.now)

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Cтатья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('post-deteil',kwargs={'pk':self.pk})