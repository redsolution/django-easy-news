# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.date_based import *
from easy_news.models import News
import datetime

archive_index_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date', 
    'template_object_name': 'news_list',
}

archive_year_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date', 
    'template_object_name': 'news',
    'make_object_list': True,
}

archive_month_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date', 
    'template_object_name': 'news',
    'month_format': '%m',
}

object_detail_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date', 
    'template_object_name': 'news',
    'month_format': '%m',
    'slug_field': 'slug',
}

object_list_dict = {
    'queryset': News.objects.filter(show=True, date__lte=datetime.datetime.now),
    'template_object_name': 'news',
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.date_based.archive_index', archive_index_dict, name='news_archive_index'),
    url(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})-(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', object_detail_dict, name='news_detail'),
    url(r'^list/$', 'django.views.generic.list_detail.object_list', object_list_dict, name='news_list'),
    url(r'^archive/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', archive_year_dict, name='news_archive_year'),
    url(r'^archive/(?P<year>\d{4})-(?P<month>\d{2})/$', 'django.views.generic.date_based.archive_month', archive_month_dict, name='news_archive_month'),
    url(r'^archive/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', archive_month_dict, name='news_archive_day'),
)
