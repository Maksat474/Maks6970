# Generated by Django 3.2.5 on 2024-02-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='#', max_length=100, verbose_name='Напишите хэштег')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование одежды')),
                ('size', models.CharField(max_length=20, verbose_name='Размер одежды')),
                ('price', models.PositiveIntegerField(verbose_name='Укажите цену продукта')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='product_cloth.Tag')),
            ],
        ),
    ]
