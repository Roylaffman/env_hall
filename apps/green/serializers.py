from apps.green import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class GreenSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Center
        geo_field = 'geom'
        fields = ('id', 'name', 'address', 'lon', 'lat', 'paper')


class StandSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Stand
        geo_field = 'geom'
        fields = ('id', 'name', 'address', 'descript')


class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produce
        fields = ('id', 'name', 'vegg', 'fruit', 'craft')


