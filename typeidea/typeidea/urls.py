import xadmin

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views

from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView, SearchView, AuthorView
)
from comment.views import CommentView
from config.views import LinkListView

from .autocomplete import CateogryAutocomplete, TagAutocomplete

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'links/$', LinkListView.as_view(), name='links'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', xadmin.site.urls, name='xadmin'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^rss|fade/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    url(r'^category-autocomplete/$', CateogryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
    url(r'ckeditor/',include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
