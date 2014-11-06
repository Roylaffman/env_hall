import os
from django.contrib.gis.utils import LayerMapping
from apps.green.models import Center

center_mapping = {
    'name' : 'name',
    'address' : 'address',
    'lon' : 'lon',
    'lat' : 'lat',
    'geom' : 'POINT',
    'glass' : 'glass',
    'paper' : 'paper',
    'aluminum' : 'aluminum',
    'plastic' : 'plastic',
    'oil' : 'oil',
    'rechargeBatteries' : 'rechargeBa',
    'electronics' : 'electronic',
    'paint' : 'paint',
    'tires' : 'tires',
    'cookGrease' : 'cookGrease',
    'scrapMetal' : 'scrapMetal',

}

center_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/centers.shp'))


def run(verbose=True):
    lm = LayerMapping(Center, center_shp, center_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
