# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from grandma.models import BaseSettings

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
