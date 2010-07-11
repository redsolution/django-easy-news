MENU_PROXY_RULES += [
    {
        'name': 'news_archive',
        'method': 'insert',
        'proxy': 'menuproxy.proxies.ReverseProxy',
        'viewname': 'news_archive_index',
        'title_text': _('news'),
    },
{% if show_years %}
        {
            'name': 'news_years',
            'method': 'children',
            'proxy': 'easy_news.menu.YearsProxy',
            'inside': 'news_archive',
            'point_function': 'easy_news.menu.year_point',
            'object_function': 'easy_news.menu.any_object',
        },
{% endif %}
{% if show_months %}
            {
                'name': 'news_monthes',
                'method': 'children',
                'proxy': 'easy_news.menu.MonthesProxy',
                'inside': 'news_years',
                'point_function': 'easy_news.menu.month_point',
                'object_function': 'easy_news.menu.any_object',
            },
{% endif %}
{% if show_days %}
                {
                    'name': 'news_days',
                    'method': 'children',
                    'proxy': 'easy_news.menu.DaysProxy',
                    'inside': 'news_monthes',
                    'point_function': 'easy_news.menu.day_point',
                    'object_function': 'easy_news.menu.any_object',
                },
{% endif %}
{% if show_details %}
                    {
                        'name': 'news_detail',
                        'method': 'children',
                        'proxy': 'easy_news.menu.NewsProxy',
                        'inside': 'news_days',
                        'point_function': 'easy_news.menu.detail_point',
                        'object_function': 'easy_news.menu.any_object',
                    },
{% endif %}
{% if show_list %}
        {
            'name': 'news_list',
            'method': 'insert',
            'proxy': 'menuproxy.proxies.ReverseProxy',
            'inside': 'news_archive',
            'viewname': 'news_list',
            'title_text': _('All news'),
        },
{% endif %}
]
EASY_NEWS_MENU_LEVEL = {{ menu_proxy_level }}
