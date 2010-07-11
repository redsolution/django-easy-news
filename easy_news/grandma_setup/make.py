from grandma.make import BaseMake
from grandma.models import GrandmaSettings
from easy_news.grandma_setup.models import EasyNewsSettings

class Make(BaseMake):
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

    def postmake(self):
        super(Make, self).make()
        easy_news_settings = EasyNewsSettings.objects.get_settings()
        grandma_settings = GrandmaSettings.objects.get_settings()
        grandma_settings.render_to('settings.py', 'easy_news/grandma/settings_menu.py', {
            'easy_news_settings': easy_news_settings,
            'show_years': easy_news_settings.menu_proxy_level > 0,
            'show_months': easy_news_settings.menu_proxy_level > 1,
            'show_days': easy_news_settings.menu_proxy_level > 2,
            'show_details': easy_news_settings.menu_proxy_level > 3,
            'show_list': easy_news_settings.menu_proxy_level > 0,
        })
