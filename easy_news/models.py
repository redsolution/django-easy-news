# -*- coding: utf-8 -*-
import datetime
from django.db import models
try:
    from tinymce.models import HTMLField
except ImportError:
    from django.db.models.fields import TextField as HTMLField

class News(models.Model):
    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ['published', 'title', ]

    title = models.CharField(max_length=200, verbose_name=u'Заголовок новости')
    slug = models.SlugField(max_length=200, verbose_name=u'Слаг', unique_for_date='date')

    date = models.DateField(verbose_name=u'Дата', default=datetime.date.today)

    short = HTMLField(verbose_name=u'Кратное описание', null=True)
    text = HTMLField(verbose_name=u'Полный текст', null=True)

    published = models.BooleanField(verbose_name=u'Опубликовано', default=True)

    def save(self, *args, **kwds):
        if self.slug is None:
            self.slug = self.id
        super(News, self).save(*args, **kwds)
    save.alters_data = True

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', [], {
            'slug': self.slug,
        })
