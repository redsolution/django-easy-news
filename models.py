# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

RU_MONTHS = [u'Января', u'Февраля', u'Марта', u'Апреля', u'Мая', u'Июня',
    u'Июля', u'Августа', u'Сентября', u'Октября', u'Ноября', u'Декабря']


class NewsItem(models.Model):
    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    title = models.CharField(max_length=200, verbose_name=u'Заголовок новости')
    slug = models.SlugField(max_length=200, verbose_name=u'Адрес', unique_for_date='date')

    date = models.DateTimeField(auto_now_add=True, editable=True, verbose_name=u'Дата')

    short = models.TextField(verbose_name=u'Кратное описание', null=True)
    text = HTMLField(verbose_name=u'Полный текст', null=True)

    published = models.BooleanField(verbose_name=u'Опубликовано', default=False)

    def rus_month(self):
        return RU_MONTHS[self.date.month - 1]

    def save(self, *args, **kwds):
        if self.slug is None:
            self.slug = '%s' % self.id
        super(NewsItem, self).save(*args, **kwds)
    save.alters_data = True

    @models.permalink
    def get_absolute_url(self):
        return ('news_item', (), {
            'slug': self.slug,
        })

