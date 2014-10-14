from apps.green import models, serializers
from rest_framework import generics
import django_filters


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split('.')]
            return qs.filter(**{'{}'.format(self.name): integers})
        return qs


class MarkerFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id')

    class Meta:
        model = models.Center
        fields = ('id', 'name')


# class CountFilter(django_filters.FilterSet):
#     id = IntegerListFilter(name='id', lookup_type='in')
#
#     class Meta:
#         model = models.County
#         fields = ['id', 'name']

class UserCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Center.objects.all()
    serializer_class = serializers.GreenSerializer
    filter_class = MarkerFilter
