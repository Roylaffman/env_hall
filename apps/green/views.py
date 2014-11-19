from django.shortcuts import render
from django.views import generic
from models import *
from forms import *
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.gis.geos import Point


def add_point(request):

    if request.method == 'POST':
        form = AddStandForm(request.POST)
        if form.is_valid():
            new_point = Stand()
            cd = form.cleaned_data
            coordinates = cd['coordinates'].split(',')
            new_point.geom = Point(float(coordinates[0]), float(coordinates[1]))
            new_point.name = cd['name']
            new_point.address = cd['address']
            new_point.descript = cd['descript']

            new_point.save()
            return HttpResponseRedirect('/add_point/success')

        else:
            return HttpResponseRedirect('/add_point/error')
    else:
        form = AddStandForm()

    args = {}
    args.update(csrf(request))
    args['form'] = AddStandForm()

    return render_to_response('green/add_point.html', args)


def form_error(request):
    return render_to_response('green/form_error.html')


def form_success(request):
    return render_to_response('green/form_success.html')


class MainView(generic.TemplateView):
    """Loads the main page."""
    template_name = 'green/main.html'


class MapView(generic.TemplateView):
    """Loads the recycling center map page."""
    template_name = 'green/center_map.html'


class ProduceMapView(generic.TemplateView):
    """Loads the produce map page."""
    template_name = 'green/produce.html'