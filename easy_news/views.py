# -*- coding: utf-8 -*-
from django.views.generic.list_detail import object_list
from easy_news.models import News
import datetime

def news_list(request):
#    this view disable queryset caching in generic view
    return object_list(request,
        queryset=News.objects.filter(show=True, date__lte=datetime.datetime.now))
