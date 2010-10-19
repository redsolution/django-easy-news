from redsolutioncms.make import BaseMake
from redsolutioncms.models import CMSSettings
from easy_news.redsolution_setup.models import EasyNewsSettings
from os.path import dirname, join


class Make(BaseMake):
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
        cms_settings.render_to(['..', 'templates', 'base_easy_news.html'],
            'easy_news/redsolutioncms/base_easy_news.html', {
            'easy_news_settings': easy_news_settings,
        }, 'w')
        
        # copy initial data fixture
        cms_settings.copy_file(
            join(cms_settings.project_dir, 'fixtures', 'initial_data.json'),
            join(dirname(__file__), 'fixtures', 'project_data', 'initial_data.json'),
            mode='a',
        )
        cms_settings.base_template = 'base_easy_news.html'
        cms_settings.save()

make = Make()
