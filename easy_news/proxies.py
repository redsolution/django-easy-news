# -*- coding: utf-8 -*-

import datetime
from django.core.urlresolvers import reverse
from django.utils.dateformat import format
from menuproxy.proxies import MenuProxy

class DatesProxy(MenuProxy):
    """Proxy to be used with menuproxy"""
    
    def __init__(self, date_field='date', **kwargs):
        super(DatesProxy, self).__init__(**kwargs)
        self.date_field = date_field 

    def title(self, obj):
        if obj is None:
            return None
        elif isinstance(obj, self.model):
            return super(DatesProxy, self).title(obj)
        type, date = obj
        if type == 'year':
            return format(date, 'Y')
        elif type == 'month':
            return format(date, 'F')
        elif type == 'day':
            return format(date, 'd')
        return ''

    def url(self, obj):
        if obj is None:
            return None
        elif isinstance(obj, self.model):
            return super(DatesProxy, self).url(obj)
        type, date = obj
        if type == 'year':
            dict = {
                'year': date.year,
            }
        elif type == 'month':
            dict = {
                'year': date.year,
                'month': date.month,
            }
        elif type == 'day':
            dict = {
                'year': date.year,
                'month': date.month,
                'day': date.day,
            }
        print type, dict
        return reverse('news_archive_%s' % type, kwargs=dict)

    def ancestors(self, obj):
        if obj is None:
            return None
        elif isinstance(obj, self.model):
            return getattr(obj, self.date_field)
        type, date = obj
        if type == 'year':
            return None
        elif type == 'month':
            return ('year', datetime.datetime(date.year, 1, 1))
        elif type == 'day':
            return ('month', datetime.datetime(date.year, date.month, 1))
        return None

    def children(self, obj):
        if obj is None:
            type, date = ('year', None)
        elif isinstance(obj, self.model):
            return None
        else:
            type, date = obj
            if type == 'year':
                type = 'month'
            elif type == 'month':
                type = 'day'
            elif type == 'day':
                type = 'object'
            else:
                return None
        lookup_kwargs = {'%s__lte' % self.date_field: datetime.datetime.now()}
        if type == 'year':
            pass
        elif type == 'month':
            lookup_kwargs['%s__year' % self.date_field] = date.year
        elif type == 'day':
            first_day = date.replace(day=1)
            if first_day.month == 12:
                last_day = first_day.replace(year=first_day.year + 1, month=1)
            else:
                last_day = first_day.replace(month=first_day.month + 1)
            lookup_kwargs['%s__gte' % self.date_field] = first_day
            lookup_kwargs['%s__lt' % self.date_field] = last_day
        elif type == 'object':
            lookup_kwargs[self.date_field] = date
        queryset = self.model.objects.filter(**lookup_kwargs)
        if type == 'object':
            return queryset
        else:
            date_list = queryset.dates(self.date_field, type)
            return [(type, date) for date in date_list] 
