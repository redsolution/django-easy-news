# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from redsolutioncms.models import CMSSettings, BaseSettings, BaseSettingsManager

class EasyNewsSettingsManager(BaseSettingsManager):
    def get_settings(self):
        if self.get_query_set().count():
            return self.get_query_set()[0]
        else:
            easy_news_settings = self.get_query_set().create()
            if easy_news_settings.model_url_was_installed():
                try:
                    from modelurl.redsolution_setup.models import ModelUrlSettings
                except ImportError:
                    pass
                else:
                    model_url_settings = ModelUrlSettings.objects.get_settings()
                    model_url_settings.models.get_or_create(model='easy_news.models.News')
            if easy_news_settings.seo_was_installed():
                try:
                    from seo.redsolution_setup.models import SeoSettings
                except ImportError:
                    pass
                else:
                    seo_settings = SeoSettings.objects.get_settings()
                    seo_settings.models.get_or_create(model='easy_news.models.News')
            if easy_news_settings.attachment_was_installed():
                try:
                    from attachment.redsolution_setup.models import AttachmentSettings
                except ImportError:
                    pass
                else:
                    attachment_settings = AttachmentSettings.objects.get_settings()
                    attachment_settings.models.get_or_create(model='easy_news.models.News')
                    attachment_settings.links.get_or_create(model='easy_news.models.News')
            if easy_news_settings.trusted_html_was_installed():
                try:
                    from trustedhtml.redsolution_setup.models import TrustedSettings
                except ImportError:
                    pass
                else:
                    trusted_settings = TrustedSettings.objects.get_settings()
                    model, _ = trusted_settings.models.get_or_create(model='easy_news.models.News')
                    model.fields.get_or_create(field='short')
                    model.fields.get_or_create(field='text')
            return easy_news_settings


class EasyNewsSettings(BaseSettings):
    MENU_PROXY_LEVELS = (
        ('0', _('Show only root')),
#        ('1', _('Show only years')),
#        ('2', _('Show years and months')),
#        ('3', _('Show years, months and days')),
        ('4', _('Show years, months, days and detail list of news')),
    )

    menu_proxy_level = models.CharField(verbose_name=_('Menu proxy level'),
        max_length=1, choices=MENU_PROXY_LEVELS, default='0')
    list_in_root = models.BooleanField(verbose_name=_('List of news in root of menu'),
        blank=True, default=True)

    def seo_was_installed(self):
        cms_settings = CMSSettings.objects.get_settings()
        return cms_settings.package_was_installed('redsolutioncms.django-seo')

    def attachment_was_installed(self):
        cms_settings = CMSSettings.objects.get_settings()
        return cms_settings.package_was_installed('redsolutioncms.django-tinymce-attachment')

    def model_url_was_installed(self):
        cms_settings = CMSSettings.objects.get_settings()
        return cms_settings.package_was_installed('redsolutioncms.django-model-url')

    def trusted_html_was_installed(self):
        cms_settings = CMSSettings.objects.get_settings()
        return cms_settings.package_was_installed('redsolutioncms.django-trusted-html')

    def menu_proxy_was_installed(self):
        cms_settings = CMSSettings.objects.get_settings()
        return cms_settings.package_was_installed('redsolutioncms.django-menu-proxy')

    def show_archive(self):
        return not self.list_in_root

    def show_root(self):
        return int(self.menu_proxy_level) >= 0

    def show_years(self):
        return int(self.menu_proxy_level) >= 1

    def show_monthes(self):
        return int(self.menu_proxy_level) >= 2

    def show_days(self):
        return int(self.menu_proxy_level) >= 3

    def show_details(self):
        return int(self.menu_proxy_level) >= 4

    def show_list(self):
        return self.show_years() and not self.list_in_root

    objects = EasyNewsSettingsManager()
