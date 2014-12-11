from django.shortcuts import render
from django.views import generic
from forms import *
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.gis.geos import Point
from apps.green import models


def add_point(request):
    """ Function used to add data to the stand model via POST."""
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


def add_prod(request):
    """ Function used to add data to produce model via POST."""
    if request.method == 'POST':
        form = AddProdForm(request.POST)
        if form.is_valid():
            new_point = Produce()
            cd = form.cleaned_data
            new_point.name = cd['name']

            new_point.vegg = cd['vegg']
            new_point.fruit = cd['fruit']
            new_point.craft = cd['craft']

            new_point.save()
            return HttpResponseRedirect('/add_point/success')

        else:
            return HttpResponseRedirect('/add_point/error')
    else:
        form = AddProdForm()

    args = {}
    args.update(csrf(request))
    args['form'] = AddProdForm()

    return render_to_response('green/add_prod.html', args)


def form_error(request):
    """ Loads this error page when there is a problem with the form the user just tried to submit."""
    return render_to_response('green/form_error.html')


def form_success(request):
    """ Loads this page when form successfully posted to the database."""
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


class ProduceInfoView(generic.ListView):
    #Does not currently load anything.  Needs to be integrated with API json data.
    model = models.Produce
    template_name = 'green/produce_stand.html'