# Generated by Django 3.2.5 on 2024-02-02 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tekken_persons', '0004_review'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Reviews',
        ),
    ]
