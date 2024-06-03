from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Имя',max_length=100)
    text = models.TextField("Описание")
    date = models.DateTimeField(default=timezone.now)
    avtor = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Таблица"
        verbose_name_plural = verbose_name


