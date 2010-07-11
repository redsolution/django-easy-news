from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from grandma.models import BaseSettings
from easy_news.grandma_setup.models import EasyNewsSettings
from django.core.exceptions import ObjectDoesNotExist

def menu_is_enabled():
    base_settings = BaseSettings.objects.get_settings()
    try:
        application = base_settings.applications.get(package='django-menu-proxy')
        return application.ok
    except ObjectDoesNotExist:
        return False

def index(request):
    easy_news_settings = EasyNewsSettings.objects.get_settings()

    exclude = []
    if not menu_is_enabled():
        exclude += ['menu_proxy_level']
    form_class = modelform_factory(EasyNewsSettings, exclude=exclude)

    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=easy_news_settings)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('custom'))
    else:
        form = form_class(instance=easy_news_settings)
    return render_to_response('easy_news/grandma/index.html', {
        'form': form,
    }, context_instance=RequestContext(request))
