from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('general.urls', namespace='general')),
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('accounts.urls', namespace='accounts')),
)
