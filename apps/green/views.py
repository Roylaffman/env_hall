from django.shortcuts import render
from django.views import generic

# Create your views here.


class MainView(generic.TemplateView):
    """Loads the main page."""
    template_name = 'green/main.html'


class MapView(generic.TemplateView):
    template_name = 'green/center_map.html'


class ProduceMapView(generic.TemplateView):
    template_name = 'green/produce.html'