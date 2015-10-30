# -*- coding: utf-8 -*-

from haystack import indexes

from easy_news.models import News


class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return News.objects.filter(show=True)