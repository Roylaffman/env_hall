from django.conf.urls import patterns, include, url
from django.contrib import admin


api_patterns = patterns('',
    url(r'^', include('apps.green.api_urls'), name='green_api')
)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'env_hall.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^green/', include('apps.green.urls', namespace='green')),
    url(r'^api/v1/', include(api_patterns, namespace='api')),
)
