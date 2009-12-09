# -*- coding: utf-8 -*-

import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.dateformat import format
from menuproxy.proxies import MenuProxy, FlatProxy, DoesNotDefined
from easy_news.models import News

EASY_NEWS_MENU_LEVEL = getattr(settings, 'EASY_NEWS_MENU_LEVEL', 3)

class RootPoint(object):
    def __init__(self, object):
        self.object = object

class BaseNewsProxy(MenuProxy):
    type = None

    def __init__(self, **kwargs):
        self.date_field = 'date'
        self.model = News
        self.children_filter = {'show': True}
        self.children_exclude = {}

    def title(self, object):
        assert object is not DoesNotDefined, DoesNotDefined
        if object is None:
            return None
        return self.title_format(object)

    def url(self, object):
        assert object is not DoesNotDefined, DoesNotDefined
        if object is None:
            return None
        return reverse('news_archive_%s' % self.type, kwargs=self.url_kwargs(object))

    def ancestors(self, object):
        return None

class YearsProxy(BaseNewsProxy):
    type = 'year'

    def title_format(self, object):
        return unicode(object)
    
    def url_kwargs(self, object):
        return {
            'year': '%04s' % object,
        }

    def children(self, object):
        if not isinstance(object, RootPoint):
            return None
        now = datetime.datetime.now()
        lookup_kwargs = {
            '%s__lte' % self.date_field: now,
        }
        result = self.model.objects.filter(**self.children_filter).exclude(**self.children_exclude).filter(
            **lookup_kwargs).dates(self.date_field, self.type)
        return [unicode(item.year)
            for item in result]

class MonthesProxy(BaseNewsProxy):
    type = 'month'
    
    def title_format(self, object):
        return format(object, 'F')
    
    def url_kwargs(self, object):
        return {
            'year': '%04d' % object.year,
            'month': '%02d' % object.month,
        }

    def children(self, object):
        if not isinstance(object, RootPoint):
            return None
        now = datetime.datetime.now()
        lookup_kwargs = {
            '%s__lte' % self.date_field: now,
            '%s__year' % self.date_field: object.object,
        }
        result = self.model.objects.filter(**self.children_filter).exclude(**self.children_exclude).filter(
            **lookup_kwargs).dates(self.date_field, self.type)
        return [datetime.date(year=item.year, month=item.month, day=item.day)
            for item in result]

class DaysProxy(BaseNewsProxy):
    type = 'day'
    
    def title_format(self, object):
        return format(object, 'j')
    
    def url_kwargs(self, object):
        return {
            'year': '%04d' % object.year,
            'month': '%02d' % object.month,
            'day': '%02d' % object.day,
        }

    def children(self, object):
        if not isinstance(object, RootPoint):
            return None
        now = datetime.datetime.now()
        first_day = object.object.replace(day=1)
        if first_day.month == 12:
            last_day = first_day.replace(year=first_day.year + 1, month=1)
        else:
            last_day = first_day.replace(month=first_day.month + 1)
        lookup_kwargs = {
            '%s__lte' % self.date_field: now,
            '%s__gte' % self.date_field: first_day,
            '%s__lt' % self.date_field: last_day,
        }
        result = self.model.objects.filter(**self.children_filter).exclude(**self.children_exclude).filter(
            **lookup_kwargs).dates(self.date_field, self.type)
        return [datetime.date(year=item.year, month=item.month, day=item.day)
            for item in result]

class NewsProxy(FlatProxy):
    def __init__(self, **kwargs):
        self.date_field = 'date'
        self.model = News
        self.children_filter = {'show': True}
        self.children_exclude = {}

    def children(self, object):
        if not isinstance(object, RootPoint):
            return None
        now = datetime.datetime.now()
        lookup_kwargs = {
            '%s__lte' % self.date_field: now,
            self.date_field: object.object,
        }
        return self.model.objects.filter(**self.children_filter).exclude(**self.children_exclude).filter(
            **lookup_kwargs)

def any_object(object, forward):
    if forward:
        return RootPoint(object)
    else:
        return DoesNotDefined

def year_point(object, forward):
    return DoesNotDefined
    
def month_point(object, forward):
    if forward:
        return DoesNotDefined
    else:
        return unicode(object.year)
    
def day_point(object, forward):
    if forward:
        return DoesNotDefined
    else:
        return object.replace(day=1)

def detail_point(object, forward):
    if forward:
        return DoesNotDefined
    else:
        object = object.date
        if EASY_NEWS_MENU_LEVEL == 4:
            return object
        object = object.replace(day=1)
        if EASY_NEWS_MENU_LEVEL == 3:
            return object
        object = unicode(object.year)
        if EASY_NEWS_MENU_LEVEL == 2:
            return object
        else:
            return DoesNotDefined 
