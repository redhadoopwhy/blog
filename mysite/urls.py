from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mysite.views import page_404

#handler404 = 'blog.views.page_404'
#handler500 = 'blog.views.page_500'
handler500 = page_404

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^$', 'mysite.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jianli', 'mysite.views.jianli'),
    url(r'^me', 'mysite.views.me'),
    url(r'^404$', 'mysite.views.page_404'),
)
