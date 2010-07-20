from django.contrib import admin
from easy_news.grandma_setup.models import EasyNewsSettings
from grandma.admin import GrandmaBaseAdmin

class EasyNewsSettingsAdmin(GrandmaBaseAdmin):
    model = EasyNewsSettings

try:
    admin.site.register(EasyNewsSettings)
except admin.sites.AlreadyRegistered:
    pass

