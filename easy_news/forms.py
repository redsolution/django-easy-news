# -*- coding: utf-8 -*-
from django import forms
from easy_news.models import News
from easy_news import settings as news_settings
from easy_news.settings import ADMIN_EXTRA_CLASS

if news_settings.NEWS_TAGGING:
    from tagging.forms import TagField


def get_extra_class(field_name):
    return ADMIN_EXTRA_CLASS.get(field_name, ADMIN_EXTRA_CLASS.get('all', ''))


class NewsAdminForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': get_extra_class('title')}),
            'author': forms.TextInput(attrs={'class': get_extra_class('author')}),
            'short': forms.Textarea(attrs={'class': get_extra_class('short')}),
            'slug': forms.TextInput(attrs={'class': get_extra_class('slug')})
        }

    if news_settings.NEWS_TAGGING:
        tags = TagField(required=False)
