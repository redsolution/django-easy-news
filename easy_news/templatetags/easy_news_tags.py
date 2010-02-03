# -*- coding: utf-8 -*-

from datetime import date, timedelta, datetime
from django import template
from django.views.generic.date_based import archive_index
from easy_news.models import News

register = template.Library()

@register.inclusion_tag('easy_news/show_news.html')
def show_news(num_latest=5):
    news_list = News.objects.filter(show=True).filter(date__lte=datetime.now()).order_by('-date')[:num_latest]
    return locals()

def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)

@register.inclusion_tag('easy_news/calendar.html')
def calendar(year=None, month=None):
    if not year:
        year = date.today().year
    if not month:
        month = date.today().month

    news_list = News.objects.filter(date__year=year, date__month=month)

    first_day_of_month = date(year, month, 1)
    last_day_of_month = get_last_day_of_month(year, month)
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())

    month_cal = []
    week = []
    week_headers = []

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['news'] = False
        for news in news_list:
            if day >= news.date and day <= news.date:
                cal_day['news'] = news
        if day.month == month:
            cal_day['in_month'] = True
        else:
            cal_day['in_month'] = False
        week.append(cal_day)
        if day.weekday() == 6:
            month_cal.append(week)
            week = []
        i += 1
        day += timedelta(1)

    return {'calendar': month_cal, 'headers': week_headers}
