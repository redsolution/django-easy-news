.. django-ordinary-news documentation master file, created by sphinx-quickstart on Tue Sep  1 12:49:12 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-ordinary-news's documentation!
================================================

Contents:

.. toctree::
   :maxdepth: 2

   install
   usage

Django ordinary news
====================

Application provides news functionality for your site.

It contains only one model

.. class:: news.models.NewsItem

    .. attribute:: title

        News title

    .. attribute:: slug

      Slug. If None provided, id attribute will be inserted while saving

    .. attribute:: date

      Publication date.

    .. attribute:: short

      Short summary of news item.

    .. attribute:: text

       Full text. TinyMCE Field used.

    ..attribute:: published

        Display this item on site or not

