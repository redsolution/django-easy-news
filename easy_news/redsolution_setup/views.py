from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from redsolutioncms.models import CMSSettings
from easy_news.redsolution_setup.models import EasyNewsSettings

from easy_news.redsolution_setup.admin import EasyNewsSettingsAdmin

def index(request):
    admin_instance = EasyNewsSettingsAdmin()
    easy_news_settings = EasyNewsSettings.objects.get_settings()
    if not easy_news_settings.menu_proxy_was_installed():
        admin_instance.exclude = ['menu_proxy_level', 'list_in_root', ]
    return admin_instance.change_view(request)
