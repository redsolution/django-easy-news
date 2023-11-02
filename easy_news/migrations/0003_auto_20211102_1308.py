# Generated by Django 2.2.24 on 2021-11-02 13:08

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_news', '0002_auto_20190821_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short',
            field=models.TextField(blank=True, default='', verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=200, unique_for_date='date', verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='main content'),
        ),
    ]