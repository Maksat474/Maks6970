from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги ')
    description = models.TextField(verbose_name='Описание книги ')
    image = models.ImageField(upload_to='')
    price = models.CharField(max_length=100, verbose_name='Цена ')
    created_at = models.DateTimeField(auto_now_add=True)