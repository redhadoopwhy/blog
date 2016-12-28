from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

handler404 = 'blog.views.page_404'
handler500 = 'blog.views.page_500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^$', 'mysite.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jianli', 'mysite.views.jianli'),
    url(r'^me', 'mysite.views.me'),
)
