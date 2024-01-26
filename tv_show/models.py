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


# class Review(models.Model):
#     tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE, related_name='tvshow_reviews')
#     text = models.TextField()
#
#     def __str__(self):
#         return self.text


class Reviews(models.Model):
    STAR = [
        ('один', 'один'),
        ('два', 'два'),
        ('три', 'три'),
        ('четыре', 'четыре'),
        ('пять', 'пять'),
    ]

    text = models.TextField()
    stars = models.TextField(choices=STAR)
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE, related_name='tvshow_reviews')

    def __str__(self):
        return self.text