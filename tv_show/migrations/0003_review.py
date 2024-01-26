# Generated by Django 3.2.5 on 2024-01-25 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0002_alter_tvshow_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('tv_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tvshow_review', to='tv_show.tvshow')),
            ],
        ),
    ]