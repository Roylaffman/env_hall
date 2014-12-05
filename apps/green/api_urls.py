from django.conf.urls import patterns, include, url
from apps.green import json_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'center', json_views.CenterCollection.as_view(), name='centers'),
    url(r'stand', json_views.StandCollection.as_view(), name='stands'),
    url(r'produce', json_views.ProduceCollection.as_view(), name='produce'),
)