from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from . import views
from .feeds import LatestPostsFeed

sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [
    url(r'^$', views.PostList, name='PostList'),
    url(r'^feeds/$', LatestPostsFeed(), name='rss'),
    url(r'^aboutme/$', views.AboutMe, name='AboutMe'),
    url(r'archives/$', views.Archives, name='Archives'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<title>[-\w]+)/$',
        views.PostDetail, name='PostDetail'),
    url(r'^categories/$', views.CateList, name='CateList'),
    url(r'^(?P<cate>[-\w]+)/$', views.CateDetail, name='CateDetail'),
    url(r'^tags/$', views.TagList, name='TagList'),
    url(r'^tags/(?P<tag>[-\w]+)/$', views.TagDetail, name='TagDetail'),
    # 后面的这几个url放在这里没有效果，要放在前面才有效果，目前不知道是什么原因
    # url(r'archives/$', views.Archives, name='Archives'),
    # url(r'^aboutme/$', views.AboutMe, name='AboutMe'),
    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='Sitemap'),
    # url(r'^feeds/$', LatestPostsFeed(), name='rss'),
]
