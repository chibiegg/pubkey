from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', 'pubkey.views.login_view', name='login_view'),
    url(r'^keys/$', 'pubkey.views.publickey_list', name='publickey_list'),
    url(r'^keys/add/$', 'pubkey.views.add_publickey', name='publickey_add'),
    url(r'^keys/edit/(\d+)/$', 'pubkey.views.add_publickey', name='publickey_edit'),
    url(r'^authorized_keys$', 'pubkey.views.authorized_keys', name='authorized_keys'),
    # url(r'^keys/$', 'pubkey.views.publickey_list', name='server_list'),
    # url(r'^keys/add/$', 'pubkey.views.add_publickey', name='server_add'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
