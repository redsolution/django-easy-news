urlpatterns += patterns('',
    (r'^news/', include('easy_news.urls'))
)
from easy_news.models import News
news_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date',
}
sitemaps['news'] = GenericSitemap(news_dict)
