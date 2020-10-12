from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation


class New(models.Model):
    title = models.CharField('Название статьи', max_length=150)
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(null=True, upload_to='media')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
class Image(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to='media')



    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения к последним событиям'

class Recent(models.Model):
    name = models.CharField('Название', max_length=150)
    image_1 = models.ImageField(null=True, blank=True, upload_to='media')
    image_2 = models.ImageField(null=True, blank=True, upload_to='media')
    image_3 = models.ImageField(null=True, blank=True, upload_to='media')
    image_4 = models.ImageField(null=True, blank=True, upload_to='media')
    image_5 = models.ImageField(null=True, blank=True, upload_to='media')
    image_6 = models.ImageField(null=True, blank=True, upload_to='media')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Последние события'
