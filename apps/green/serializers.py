from apps.green import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class GreenSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Center
        geo_field = 'geom'
        fields = ('id', 'name', 'address', 'lon', 'lat')


class StandSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Stand
        geo_field = 'geom'
        fields = ('id', 'address', 'lon', 'lat', 'descript')

# class CountySerializer(geoserializers.GeoFeatureModelSerializer):
#     class Meta:
#         model = models.County
#         geo_field = 'geom'
#         fields = ('id', 'name')
