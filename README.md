# django-easy-news

Application provides news functionality for your site.

## Installation and basic usage


1. Install package

    `` pip install git+git://github.com/oldroute/django-easy-news.git``


2. Configure your settings file:

	``INSTALLED_APPS += ['easy_news']``


3. Add urlpattern to main urls.py:

    ```python
    urlpatterns = [
	...
        url(r'^news/', include('easy_news.urls')),
    ...
    ```
7. Apply migrations and run local server

    ```python
    python manage.py migrate easy_news
    python manage.py runserver
    ```

### Views

Easy news has several url handlers (I mean named patterns):

- ``news_detail`` - show news itself
- ``news_list`` - shows list of publicated news if ``settings.ENABLE_NEWS_LIST`` is True
- ``news_archive_index`` - shows content of ``django.views.generic.date_based.archive_index_view`` if ``news_settings.ENABLE_NEWS_ARCHIVE_INDEX`` is True
- ``news_archive_year``, ``news_archive_month``, ``news_archive_day`` - shows news archive by given date, if ``settings.ENABLE_NEWS_DATE_ARCHIVE`` is True
- ``news_tag_detail`` - if you use ``django-tagging`` and ``settings.NEWS_TAGGING`` is True, easy_news provide list of tagged news

### Templatetags

- ``{% show_news <num> %}`` - render list of ``num`` latest news.(default: 5) with template ``easy_news/parts/block.html``

- ``{% get_news <num> %}`` - return queryset of ``num`` latest news. (default: all)

- ``{% calendar <year> <month> %}`` - render calendar with template ``easy_news/parts/calendar.html``. If there's some news at date, shows hyperlink to news (by default, use current date)

Customize:
----------

Full settings list:

- ``ENABLE_NEWS_LIST`` (boolean) - render latest news list. Default - True
- ``ENABLE_NEWS_ARCHIVE_INDEX`` (boolean) - render django generic date **archive index** of news objects. Default - True
- ``ENABLE_NEWS_DATE_ARCHIVE`` (boolean) - render django generic date **full archive** of news objects. Default - True
- ``NEWS_TAGGING`` (boolean) - use news tagging. Default - if `django-tagging`_ is installed, True, otherwise False
- ``NEWS_ADMIN_EXTRA_CLASS`` - Admin page customizing: dictionary of extra css classes for fields. Default - ``{'all': ''}``
- ``NEWS_ADMIN_EXTRA_CSS`` - Admin page customizing: dictionary of extra css files for mailing list admin page. Default - `` {'all': ['']})``

	Example:
	```python
	NEWS_ADMIN_EXTRA_CLASS = {'all': 'my-class'}
    NEWS_ADMIN_EXTRA_CSS = {'all': ['css/admin/common.css']}``
	```

HISTORY:
--------
0.2.3: Added haystack compatibility

Classifiers:

`Frontpage handlers`_

.. _`django generic views system`: http://docs.djangoproject.com/en/1.2/ref/generic-views/
.. _`django.views.generic.date_based.archive_index`: http://docs.djangoproject.com/en/1.2/ref/generic-views/#django-views-generic-date-based-archive-index
.. _`django-tagging`: http://pypi.python.org/pypi/django-tagging/
.. _`Frontpage handlers`: http://www.redsolutioncms.org/classifiers/frontpage

0.3.0: Added support for django 1.7

- Delete support menu proxy

1.11: Added support for django 1.11
- Added templatetag "get_news"
- Update template structure
- News model: new fields - "show", "creation_date", "author"; new properties - "main_content", "short_description"
