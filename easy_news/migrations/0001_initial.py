# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tinymce.models

from easy_news import settings

if settings.NEWS_TAGGING:
    from tagging.fields import TagField

fields = [
    ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
    ('title', models.CharField(max_length=500, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043d\u043e\u0432\u043e\u0441\u0442\u0438')),
    ('slug', models.SlugField(max_length=200, verbose_name='\u0421\u043b\u0430\u0433', unique_for_date=b'date')),
    ('date', models.DateField(default=datetime.date.today, verbose_name='\u0414\u0430\u0442\u0430')),
    ('short', tinymce.models.HTMLField(default=b'', verbose_name='\u041a\u0440\u0430\u0442\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
    ('text', tinymce.models.HTMLField(default=b'', verbose_name='\u041f\u043e\u043b\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442', blank=True)),
    ('show', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
]

if settings.NEWS_TAGGING:
    fields.append(('tags', TagField(null=True)))


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=fields,
            options={
                'ordering': ['-date', 'title'],
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
            bases=(models.Model,),
        ),
    ]
