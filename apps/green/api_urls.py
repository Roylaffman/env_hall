from django.conf.urls import patterns, include, url
from apps.green import json_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'green', json_views.CenterCollection.as_view(), name='centers'),
)