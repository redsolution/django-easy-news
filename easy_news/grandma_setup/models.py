# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from grandma.models import GrandmaSettings, BaseSettings, BaseSettingsManager

class EasyNewsSettingsManager(BaseSettingsManager):
    def get_settings(self):
        if self.get_query_set().count():
            return self.get_query_set()[0]
        else:
            grandma_settings = GrandmaSettings.objects.get_settings()
            if grandma_settings.package_was_installed('grandma.django-model-url'):
                try:
                    from modelurl.grandma_setup.models import ModelUrlSettings
                except ImportError:
                    pass
                else:
                    model_url_settings = ModelUrlSettings.objects.get_settings()
                    model_url_settings.models.get_or_create(model='easy_news.models.News')
                    # TODO:
                    # model_url_settings.views.get_or_create(view='django.views.generic.date_based.object_detail', object='object')
            if grandma_settings.package_was_installed('grandma.django-seo'):
                try:
                    from seo.grandma_setup.models import SeoSettings
                except ImportError:
                    pass
                else:
                    seo_settings = SeoSettings.objects.get_settings()
                    seo_settings.models.get_or_create(model='easy_news.models.News')
            if grandma_settings.package_was_installed('grandma.django-tinymce-attachment'):
                try:
                    from attachment.grandma_setup.models import AttachmentSettings
                except ImportError:
                    pass
                else:
                    attachment_settings = AttachmentSettings.objects.get_settings()
                    attachment_settings.models.get_or_create(model='easy_news.models.News')
                    attachment_settings.links.get_or_create(model='easy_news.models.News')
            if grandma_settings.package_was_installed('grandma.django-trusted-html'):
                try:
                    from trustedhtml.grandma_setup.models import TrustedSettings
                except ImportError:
                    pass
                else:
                    trusted_settings = TrustedSettings.objects.get_settings()
                    model, _ = trusted_settings.models.get_or_create(model='easy_news.models.News')
                    model.fields.get_or_create(field='short')
                    model.fields.get_or_create(field='text')
            return self.get_query_set().create()


class EasyNewsSettings(BaseSettings):
    MENU_PROXY_LEVELS = (
        ('0', _('Don`t show')),
        ('1', _('Show only years')),
        ('2', _('Show years and months')),
        ('3', _('Show years, months and days')),
        ('4', _('Show years, months, days and list of news')),
    )
    menu_proxy_level = models.CharField(verbose_name=_('Menu proxy level'),
        max_length=1, choices=MENU_PROXY_LEVELS, default='3')

    objects = EasyNewsSettingsManager()
