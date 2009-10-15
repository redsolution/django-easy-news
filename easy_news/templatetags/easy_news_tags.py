# -*- coding: utf-8 -*-

import datetime
from django import template
from django.views.generic.date_based import archive_index
from easy_news.models import News

register = template.Library()

@register.inclusion_tag('easy_news/show_news.html')
def show_news(num_latest=5):
    news_list = News.objects.filter(show=True).filter(date__lte=datetime.datetime.now()).order_by('-date')[:num_latest]
    return locals()
