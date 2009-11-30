# -*- coding: utf-8 -*-

import datetime
from django.core.urlresolvers import reverse
from django.utils.dateformat import format
from menuproxy.proxies import MenuProxy, FlatProxy, DoesNotDefined
from easy_news.models import News

class BaseNewsProxy(MenuProxy):
    type = None
    title_format = None
    url_fields = []

    def __init__(self, **kwargs):
        self.date_field = 'date'
        self.model = News
        self.children_filter = {'show': True}
        self.children_exclude = {}

    def title(self, object):
        assert object is not DoesNotDefined, DoesNotDefined
        if object is None:
            return None
        return format(object, self.title_format)

    def url(self, object):
        assert object is not DoesNotDefined, DoesNotDefined
        if object is None:
            return None
        kwargs = {}
        for field in self.url_fields:
            kwargs[field] = getattr(object, field)
        return reverse('news_archive_%s' % self.type, kwargs=kwargs)

    def ancestors(self, object, menu_item):
        return None

class YearsProxy(BaseNewsProxy):
    type = 'year'
    title_format = 'Y'
    url_fields = ['year', ]
    
    def children(self, object, menu_item):
        if object is not DoesNotDefined:
            return None
        now = datetime.datetime.now()
        lookup_kwargs = {
            '%s__lte' % self.date_field: now,
        }
        return self.model.objects.filter(**self.children_filter).exclude(**self.children_exclude).filter(
            **lookup_kwargs).dates(self.date_field, self.type)

class MonthesProxy(BaseNewsProxy):
    type = 'month'
    title_format = 'F'
    url_fields = ['year', 'month', ]
    
    def children(self, object, menu_item):
        if object is not DoesNotDefined:
            return None
        now = datetime.datetime.now()
        lookup_kwargs = {
            '%s__lte' % self.date_field: now,
            '%s__year' % self.date_field: menu_item.object.year,
        }
        return self.model.objects.filter(**self.children_filter).exclude(**self.children_exclude).filter(
            **lookup_kwargs).dates(self.date_field, self.type)

class DaysProxy(BaseNewsProxy):
    type = 'day'
    title_format = 'd'
    url_fields = ['year', 'month', 'day', ]
    
    def children(self, object, menu_item):
        if object is not DoesNotDefined:
            return None
        now = datetime.datetime.now()
        first_day = menu_item.object.replace(day=1)
        if first_day.month == 12:
            last_day = first_day.replace(year=first_day.year + 1, month=1)
        else:
            last_day = first_day.replace(month=first_day.month + 1)
        lookup_kwargs = {
            '%s__lte' % self.date_field: now,
            '%s__gte' % self.date_field: first_day,
            '%s__lt' % self.date_field: last_day,
        }
        return self.model.objects.filter(**self.children_filter).exclude(**self.children_exclude).filter(
            **lookup_kwargs).dates(self.date_field, self.type)

class NewsProxy(FlatProxy):
    def __init__(self, **kwargs):
        self.date_field = 'date'
        self.model = News
        self.children_filter = {'show': True}
        self.children_exclude = {}

    def children(self, object, menu_item):
        if object is not DoesNotDefined:
            return None
        now = datetime.datetime.now()
        lookup_kwargs = {
            '%s__lte' % self.date_field: now,
            self.date_field: menu_item.object,
        }
        return self.model.objects.filter(**self.children_filter).exclude(**self.children_exclude).filter(
            **lookup_kwargs)
