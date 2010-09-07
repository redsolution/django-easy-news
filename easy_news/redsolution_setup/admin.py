from django.contrib import admin
from easy_news.redsolution_setup.models import EasyNewsSettings

try:
    admin.site.register(EasyNewsSettings)
except admin.sites.AlreadyRegistered:
    pass
