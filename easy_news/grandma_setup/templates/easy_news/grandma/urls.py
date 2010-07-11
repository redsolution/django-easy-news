urlpatterns += patterns('',
    (r'^news/', include('easy_news.urls'))
)
news_dict = {
    'queryset': News.objects.filter(show=True),
    'date_field': 'date',
}
sitemaps['news'] = GenericSitemap(news_dict),
