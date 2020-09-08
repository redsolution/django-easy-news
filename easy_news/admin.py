# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import News
from .forms import NewsAdminForm
from easy_news import settings as news_settings


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    # @property
    # def media(self):
    #     media = super(NewsAdmin, self).media
    #     media.add_css(news_settings.ADMIN_EXTRA_CSS)
    #     return media

    list_filter = ['show']
    search_fields = ['title', 'short', 'text', 'author']
    list_display = ['title', 'date', 'show', 'author']
    prepopulated_fields = {'slug': ('title',)}
    model = News
    form = NewsAdminForm

