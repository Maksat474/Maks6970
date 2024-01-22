from django.db import models


class TVShow(models.Model):
    CATEGORY = (
        ('Боевик', 'Боевик'),
        ('Детектив', 'Детектив'),
        ('Комедия', 'Комедия'),
        ('Фантастика', 'Фантастика'),
        ('Ужас', 'Ужас'),
    )
    name = models.CharField(max_length=100, verbose_name='Укажите название шоу')
    description = models.TextField(verbose_name='Укажите описание шоу')
    image = models.URLField(verbose_name='Вставьте ссылку на фото')
    category = models.CharField(max_length=100, choices=CATEGORY, verbose_name='Выберите категорию фильма')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.category}'

    class Meta:
        verbose_name = 'ТВ шоу'
        verbose_name_plural = 'ТВ шоу'