# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.db import models, migrations

from easy_news import settings


class Migration(migrations.Migration):
    dependencies = [
        ('easy_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='News',
            name='author',
            field=models.CharField(max_length=100, verbose_name='\u0410\u0432\u0442\u043E\u0440', null=True, blank=True),
            preserve_default=True,
        )
    ]