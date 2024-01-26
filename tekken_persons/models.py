from django.db import models


class PersonGame(models.Model):
    SPORT = (
        ('Каратэ', 'Каратэ'),
        ('Кунг-фу', 'Кунг-фу'),
        ('Муай-тай', 'Муай-тай'),
        ('Бокс', 'Бокс'),
        ('Кикбокс', 'Кикбокс'),
        ('Рестлинг', 'Рестлинг'),
        ('Нинзитсу', 'Нинзитсу')
    )
    name = models.CharField(max_length=50, verbose_name='Укажите имя игрока', null=True)
    email = models.EmailField(verbose_name='Укажите почту', blank=True)
    description = models.TextField(verbose_name='кажите описание', blank=True, null=True)
    age = models.PositiveIntegerField(default=15, verbose_name='Укажите возраст игрока')
    image = models.URLField(verbose_name='Вставьте ссылку на фото')
    capabilities = models.CharField(max_length=100, verbose_name='Укажите способность персонажа')
    sport = models.CharField(max_length=100, choices=SPORT, verbose_name='Выберите спорт персонажа')
    video_url = models.URLField(verbose_name='Вставьте ссылку с ютуб')

    def __str__(self):
        return f'{self.name}-{self.sport}'

    class Meta:
        verbose_name = 'Персонажа'
        verbose_name_plural = 'Персонажи'


class Review(models.Model):
    tekken_person = models.ForeignKey(PersonGame, on_delete=models.CASCADE, related_name='tekken_review')
    text = models.TextField()

    def __str__(self):
        return self.text