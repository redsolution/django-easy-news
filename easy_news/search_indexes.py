# -*- coding: utf-8 -*-

from haystack import indexes
from haystack import site

from easy_news.models import News

class NewsIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return News.objects.filter(show=True)

site.register(News, NewsIndex)
