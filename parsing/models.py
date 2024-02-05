from django.db import models


class KivanoNouts(models.Model):
    title = models.CharField(max_length=500)
    price = models.CharField(max_length=30)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

