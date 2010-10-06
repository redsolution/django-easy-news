from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from easy_news.redsolution_setup.models import EasyNewsSettings
from easy_news.redsolution_setup.admin import EasyNewsSettingsAdmin
from redsolutioncms.models import CMSSettings

def index(request):
    admin_instance = EasyNewsSettingsAdmin()
    easy_news_settings = EasyNewsSettings.objects.get_settings()
    cms_settings = CMSSettings.objects.get_settings()
    if not 'redsolutioncms.django-menu-proxy' in cms_settings.installed_packages:
        admin_instance.exclude = ['menu_proxy_level', 'list_in_root', ]
    return admin_instance.change_view(request)
