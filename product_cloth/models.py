from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Напишите хэштег', default='#')

    def __str__(self):
        return self.name


class ProductCloth(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование одежды')
    size = models.CharField(max_length=20, verbose_name='Размер одежды')
    price = models.PositiveIntegerField('Укажите цену продукта')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title