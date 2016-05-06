from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',

    url(r'^login/$', 'login_index', name='accounts_login_index'),
    url(r'^register/$', 'register_index', name='accounts_register_index'),
    #url(r'^logout/$', 'logout_index', name="accounts_logout_index"),
)