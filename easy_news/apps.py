from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NewsAppConfig(AppConfig):
    name = 'easy_news'
    verbose_name = _('News')