================
django-easy-news
================

Application provides news functionality for your site.

Installation:
=============

In settings.py:
---------------

1. Add ``easy_news`` to your ``INSTALLED_APPS``.

2. Include ``('easy_news.urls')`` in your ``urls.py`` like this::

    urlpatterns += patterns('',
        (r'^news/', include('easy_news.urls')),
    )

Usage
======

Views
------
Easy news uses `django generic views system`_ to render pages. 
Easy news has several url handlers (I mean named patterns):

- ``news_detail`` - Show news itself
- ``news_list`` - if ``settings.ENABLE_NEWS_LIST`` is True, shows list of publicated news
- ``news_archive_index`` if ``news_settings.ENABLE_NEWS_ARCHIVE_INDEX`` is True, shows content of `django.views.generic.date_based.archive_index`_ view
- ``news_archive_year``, ``news_archive_month``, ``news_archive_day`` - if ``settings.ENABLE_NEWS_DATE_ARCHIVE`` is True, shows news archive by given date
- ``news_tag_detail`` - if you use ``django-tagging`` and ``settings.NEWS_TAGGING`` is True, easy_news provide list of tagged news  

Template tags:
--------------

If you want to use easy_news template tags, load ``easy_news_tags``::

    {% load menuproxy_tags %}

show_news
``````````

Shows list of ``num`` latest news. 5 news in list by default:: 

    {% show_news <num> %}

calendar
````````

Render calendar. If there's some news at date, shows hyperlink to news. By default, use current date::

    {% calendar <year> <month> %}
    
Customize:
----------

Full settings list:

- ``ENABLE_NEWS_LIST`` (boolean) - render latest news list. Default - True
- ``ENABLE_NEWS_ARCHIVE_INDEX`` (boolean) - render django generic date **archive index** of news objects. Default - True
- ``ENABLE_NEWS_DATE_ARCHIVE`` (boolean) - render django generic date **full archive** of news objects. Default - True
- ``NEWS_TAGGING`` (boolean) - use news tagging. Default - if `django-tagging`_ is installed, True, otherwise False

Classifiers:
-------------

`Frontpage handlers`_

.. _`django generic views system`: http://docs.djangoproject.com/en/1.2/ref/generic-views/
.. _`django.views.generic.date_based.archive_index`: http://docs.djangoproject.com/en/1.2/ref/generic-views/#django-views-generic-date-based-archive-index
.. _`django-tagging`: http://pypi.python.org/pypi/django-tagging/
.. _`Frontpage handlers`: http://www.redsolutioncms.org/classifiers/frontpage