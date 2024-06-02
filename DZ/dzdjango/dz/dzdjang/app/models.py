from django.db import models
class newtable(models.Model):
    name = models.CharField('Имя',max_length=100)
    text = models.TextField("Описание")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Таблица"
        verbose_name_plural = verbose_name
