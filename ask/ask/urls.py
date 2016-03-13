from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test, popular, question, ask, ans
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$' , test, name='test'),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<post_id>\d+)/$', question, name='question'),
    url(r'^ask/', ask),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
    url(r'^answer/$', ans)
)
