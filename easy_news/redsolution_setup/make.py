from redsolutioncms.make import BaseMake
from redsolutioncms.models import CMSSettings
from easy_news.redsolution_setup.models import EasyNewsSettings
from django.template.loader import render_to_string

class Make(BaseMake):
    def premake(self):
        super(Make, self).premake()
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.right_blocks.create(html=
            render_to_string('easy_news/redsolutioncms/right.html'))

    def make(self):
        super(Make, self).make()
        easy_news_settings = EasyNewsSettings.objects.get_settings()
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.render_to('settings.py', 'easy_news/redsolutioncms/settings.pyt', {
            'easy_news_settings': easy_news_settings,
        })
        cms_settings.render_to('urls.py', 'easy_news/redsolutioncms/urls.pyt', {
            'easy_news_settings': easy_news_settings,
        })
        cms_settings.render_to(['..', 'templates', 'easy_news', 'news_detail.html'],
            'easy_news/redsolutioncms/news_detail.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        cms_settings.render_to(['..', 'templates', 'easy_news', 'news_archive.html'],
            'easy_news/redsolutioncms/news_archive.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        cms_settings.render_to(['..', 'templates', 'easy_news', 'news_archive_day.html'],
            'easy_news/redsolutioncms/news_archive_day.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        cms_settings.render_to(['..', 'templates', 'easy_news', 'news_archive_month.html'],
            'easy_news/redsolutioncms/news_archive_month.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        cms_settings.render_to(['..', 'templates', 'easy_news', 'news_archive_year.html'],
            'easy_news/redsolutioncms/news_archive_year.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        cms_settings.render_to(['..', 'templates', 'easy_news', 'news_list.html'],
            'easy_news/redsolutioncms/news_list.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')

    def postmake(self):
        super(Make, self).postmake()
        easy_news_settings = EasyNewsSettings.objects.get_settings()
        if not easy_news_settings.menu_proxy_was_installed():
            return
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.render_to('settings.py', 'easy_news/redsolutioncms/settings_menu.pyt', {
            'easy_news_settings': easy_news_settings,
        })

make = Make()