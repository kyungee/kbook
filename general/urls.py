from django.conf.urls import patterns, url


urlpatterns = patterns('general.views',
    url(r'^$', 'index', name='index'),
)