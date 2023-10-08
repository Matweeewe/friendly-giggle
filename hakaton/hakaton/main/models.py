from django.db import models


class Tiket(models.Model):
    objeckts = None
    title = models.CharField('Название', max_length=50)
    tiket = models.TextField('Описание(не более 50 символов)')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"