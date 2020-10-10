from django.db import models
from django.contrib.auth.models import User

class Introduction(models.Model):
    name = models.CharField('ФИО', max_length=50)
    klass = models.CharField('Класс', max_length=50)
    phone = models.IntegerField('Контактный номер телефона')
    email = models.EmailField('Email', default="")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
