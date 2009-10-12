# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from news.models import NewsItem
from django.views.generic.date_based import *


news_dict = {
    'queryset': NewsItem.objects.filter(published=True),
}

news_date_dict = news_dict.copy()
news_date_dict.update({
    'date_field': 'date',
})

news_date_dict_month = news_date_dict.copy()
news_date_dict_month.update({
    'month_format': '%m',
})

urlpatterns = patterns('django.views.generic',
    url(r'^$', 'date_based.archive_index', news_date_dict, name='news_archive_index'),
    url(r'^(?P<year>\d{4})/$', 'date_based.archive_year', news_date_dict, name='news_archive_year'),
    url(r'^(?P<year>\d{4})-(?P<month>\d{2})/$', 'date_based.archive_month',news_date_dict_month, name='news_archive_month'),
    url(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{1,2})/$', 'date_based.archive_day', news_date_dict_month, name='news_archive_day'),
    # we can't assign news_item view to date_based.object_detail 
    # because it can't be reversed in get_absolute_url(). Maybe I'm wrong.
    url(r'^(?P<slug>\w+)/$', 'list_detail.object_detail', news_dict, name='news_item'),
)
