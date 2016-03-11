from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test, popular, question
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$' , test, name='test'),
    url(r'^login/$', test),
    url(r'^sigup/$', test),
    url(r'^question/(?P<id>\d+)/$', question),
    url(r'^ask/', test),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
)
