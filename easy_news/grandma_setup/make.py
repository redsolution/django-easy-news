import os
from grandma.make import BaseMake
from grandma.models import GrandmaSettings
from easy_news.grandma_setup.models import EasyNewsSettings
from django.template.loader import render_to_string

class Make(BaseMake):
    def premake(self):
        super(Make, self).premake()
        grandma_settings = GrandmaSettings.objects.get_settings()
        grandma_settings.right_blocks.create(html=
            render_to_string('easy_news/grandma/right.html'))

    def make(self):
        super(Make, self).make()
        easy_news_settings = EasyNewsSettings.objects.get_settings()
        grandma_settings = GrandmaSettings.objects.get_settings()
        grandma_settings.render_to('settings.py', 'easy_news/grandma/settings.py', {
            'easy_news_settings': easy_news_settings,
        })
        grandma_settings.render_to('urls.py', 'easy_news/grandma/urls.py', {
            'easy_news_settings': easy_news_settings,
        })
        grandma_settings.render_to(os.path.join('..', 'templates', 'easy_news', 'news_detail.html'),
            'easy_news/grandma/news_detail.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        grandma_settings.render_to(os.path.join('..', 'templates', 'easy_news', 'news_archive.html'),
            'easy_news/grandma/news_archive.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        grandma_settings.render_to(os.path.join('..', 'templates', 'easy_news', 'news_archive_day.html'),
            'easy_news/grandma/news_archive_day.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        grandma_settings.render_to(os.path.join('..', 'templates', 'easy_news', 'news_archive_month.html'),
            'easy_news/grandma/news_archive_month.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        grandma_settings.render_to(os.path.join('..', 'templates', 'easy_news', 'news_archive_year.html'),
            'easy_news/grandma/news_archive_year.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        grandma_settings.render_to(os.path.join('..', 'templates', 'easy_news', 'news_list.html'),
            'easy_news/grandma/news_list.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')

    def postmake(self):
        super(Make, self).postmake()
        grandma_settings = GrandmaSettings.objects.get_settings()
        if not grandma_settings.package_was_installed('grandma.django-menu-proxy'):
            return
        easy_news_settings = EasyNewsSettings.objects.get_settings()
        grandma_settings.render_to('settings.py', 'easy_news/grandma/settings_menu.py', {
            'easy_news_settings': easy_news_settings,
        })
