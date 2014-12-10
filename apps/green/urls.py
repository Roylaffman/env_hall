from django.conf.urls import patterns, include, url
from apps.green import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', views.MainView.as_view(), name='main'),
    url(r'^center_map/', views.MapView.as_view(), name='center_map'),
    url(r'^produce/', views.ProduceMapView.as_view(), name='produce'),
    url(r'produce_stand/$', views.ProduceInfoView.as_view(), name="produce_stand"),

)
