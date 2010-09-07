from django.contrib import admin
from easy_news.redsolution_setup.models import EasyNewsSettings
from redsolutioncms.admin import CMSBaseAdmin

class EasyNewsSettingsAdmin(CMSBaseAdmin):
    model = EasyNewsSettings

try:
    admin.site.register(EasyNewsSettings)
except admin.sites.AlreadyRegistered:
    pass
