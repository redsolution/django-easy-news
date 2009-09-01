# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from news.models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    class NewsItemForm(forms.ModelForm):
        class Meta:
            model = NewsItem
        title = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    model = NewsItem
    list_display = ['title', 'date', 'published',]
    prepopulated_fields = {'slug': ('title',)}
    form = NewsItemForm


try:
    admin.site.register(NewsItem, NewsItemAdmin)
except admin.sites.AlreadyRegistered:
    pass
