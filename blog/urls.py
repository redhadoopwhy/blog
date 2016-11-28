from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.blog_index, name='index'),
    url(r'^(?P<blog_id>[0-9]*)/$', views.blog_bond, name='blog'),
    url(r'^tag/', views.blog_tag, name='tag'),
    url(r'^tag(?P<blog_tag>[0-9]*)/$', views.blog_bond_tag, name='blog_tag'),
    url(r'^post/', views.blog_post, name='postblog'),
    url(r'^blog_post_add/', views.blog_post_add, name='blog_post_add'),
    url(r'^search', views.blog_search, name='blog_search')
]
