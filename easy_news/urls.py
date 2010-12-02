# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.date_based import *
from easy_news.models import News
import datetime

from easy_news import settings as news_settings
archive_index_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date',
    'template_object_name': 'object_list',
}

archive_year_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date',
    'make_object_list': True,
}

archive_month_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date',
    'month_format': '%m',
}

object_detail_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date',
    'month_format': '%m',
    'slug_field': 'slug',
}

urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})-(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', object_detail_dict, name='news_detail'),
)

if news_settings.ENABLE_NEWS_LIST:
    urlpatterns += patterns('',
        url(r'^list/$', 'easy_news.views.news_list', name='news_list'),
    )

if news_settings.ENABLE_NEWS_ARCHIVE_INDEX:
    urlpatterns += patterns('',
        url(r'^$', 'django.views.generic.date_based.archive_index', archive_index_dict, name='news_archive_index'),
    )

if news_settings.ENABLE_NEWS_DATE_ARCHIVE:
    urlpatterns += patterns('',
        url(r'^archive/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', archive_year_dict, name='news_archive_year'),
        url(r'^archive/(?P<year>\d{4})-(?P<month>\d{2})/$', 'django.views.generic.date_based.archive_month', archive_month_dict, name='news_archive_month'),
        url(r'^archive/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', archive_month_dict, name='news_archive_day'),
    )

if news_settings.NEWS_TAGGING:
    from tagging.views import tagged_object_list
    urlpatterns += patterns('',
        url(r'^tag/(?P<tag>[^/]+)/$', tagged_object_list,
            dict(queryset_or_model=News.objects.filter(show=True), paginate_by=10, allow_empty=True), name='news_tag_detail'),
    )
