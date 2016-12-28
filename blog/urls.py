#coding=utf-8
from django.conf.urls import url, patterns
from blog import views

urlpatterns = [
    url(r'^$', views.blog_index, name='index'),					#主页(分页显示)	
    url(r'^(?P<blog_id>[0-9]*)/$', views.blog_bond, name='blog'),		#每个blog
    url(r'^tag/', views.blog_tag, name='tag'),					#标签
    url(r'^tag(?P<blog_tag>[0-9]*)/$', views.blog_bond_tag, name='blog_tag'),	#每个标签的blog
    url(r'^post/', views.blog_post, name='postblog'),				#添加blog页面	
    url(r'^blog_post_add/', views.blog_post_add, name='blog_post_add'),		#添加blog跳转
    url(r'^search', views.blog_search, name='blog_search'),			#搜索结果页
    url(r'^postlogin/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^postlogout/$', 'django.contrib.auth.views.logout', {'template_name': 'index.html'}),
]
