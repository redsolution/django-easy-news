# ---- easy-news ----

INSTALLED_APPS += ['easy_news']

{% if 'redsolutioncms.django-menu-proxy' in cms_settings.installed_packages %}
try:
    MENU_PROXY_RULES
except NameError:
    MENU_PROXY_RULES = []

{% if easy_news_settings.show_root %}
MENU_PROXY_RULES += [{% if easy_news_settings.list_in_root %}
    {
        'name': 'news_list',
        'method': 'insert',
        'proxy': 'menuproxy.proxies.ReverseProxy',
        'viewname': 'news_list',
        'title_text': gettext_noop('All news'),
    },
{% else %}
    {
        'name': 'news_archive',
        'method': 'insert',
        'proxy': 'menuproxy.proxies.ReverseProxy',
        'viewname': 'news_archive_index',
        'title_text': gettext_noop('news'),
    },
{% endif %}{% if easy_news_settings.show_years %}
        {
            'name': 'news_years',
            'method': 'children',
            'proxy': 'easy_news.menu.YearsProxy',
            'inside': {% if easy_news_settings.list_in_root %}'news_list'{% else %}'news_archive'{% endif %},
            'point_function': 'easy_news.menu.year_point',
            'object_function': 'easy_news.menu.any_object',
        },
{% endif %}{% if easy_news_settings.show_monthes %}
            {
                'name': 'news_monthes',
                'method': 'children',
                'proxy': 'easy_news.menu.MonthesProxy',
                'inside': 'news_years',
                'point_function': 'easy_news.menu.month_point',
                'object_function': 'easy_news.menu.any_object',
            },
{% endif %}{% if easy_news_settings.show_days %}
                {
                    'name': 'news_days',
                    'method': 'children',
                    'proxy': 'easy_news.menu.DaysProxy',
                    'inside': 'news_monthes',
                    'point_function': 'easy_news.menu.day_point',
                    'object_function': 'easy_news.menu.any_object',
                },
{% endif %}
                    {
                        'name': 'news_detail',
                        'method': 'children',
                        'proxy': 'easy_news.menu.NewsProxy',
                        'inside': {% if easy_news_settings.show_days %}'news_days',
                        'point_function': 'easy_news.menu.detail_point',
                        'object_function': 'easy_news.menu.any_object',
{% else %}{% if easy_news_settings.show_monthes %}'news_monthes',
                        'point_function': 'easy_news.menu.detail_point',
                        'object_function': 'easy_news.menu.any_object',
{% else %}{% if easy_news_settings.show_years %}'news_years',
                        'point_function': 'easy_news.menu.detail_point',
                        'object_function': 'easy_news.menu.any_object',
{% else %}{% if easy_news_settings.list_in_root %}'news_list',
{% else %}'news_archive',
{% endif %}{% endif %}{% endif %}{% endif %}                        
                    },
{% if easy_news_settings.show_list %}
        {
            'name': 'news_list',
            'method': 'insert',
            'proxy': 'menuproxy.proxies.ReverseProxy',
            'inside': 'news_archive',
            'viewname': 'news_list',
            'title_text': gettext_noop('All news'),
        },
{% endif %}]
EASY_NEWS_MENU_LEVEL = {{ easy_news_settings.menu_proxy_level }}
{% endif %}
{% endif %}
