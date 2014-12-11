from apps.green import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class GreenSerializer(geoserializers.GeoFeatureModelSerializer):
    """ Serializer used in API set up off the Center model."""
    class Meta:
        model = models.Center
        geo_field = 'geom'
        fields = ('id', 'name', 'address', 'lon', 'lat', 'paper', 'glass', 'aluminum', 'plastic', 'oil', 'rechargeBatteries',
                  'electronics', 'paint', 'tires', 'cookGrease', 'scrapMetal')


class StandSerializer(geoserializers.GeoFeatureModelSerializer):
    """ Serializer used in API set up of the Stand model."""
    class Meta:
        model = models.Stand
        geo_field = 'geom'
        fields = ('id', 'name', 'address', 'descript')


class ProduceSerializer(serializers.ModelSerializer):
    """ Serializer used in API set up of the Produce model."""
    class Meta:
        model = models.Produce
        fields = ('id', 'name', 'vegg', 'fruit', 'craft')


