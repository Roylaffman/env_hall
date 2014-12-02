from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.contrib.auth.decorators import login_required


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
    url(r'^add_point/$', 'apps.green.views.add_point'),
    url(r'^add_point/error$', 'apps.green.views.form_error'),
    url(r'^add_point/success$', 'apps.green.views.form_success'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
