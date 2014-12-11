from apps.green import models, serializers
from rest_framework import generics
import django_filters


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split('.')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type): integers})
        return qs


class MarkerFilter(django_filters.FilterSet):
    """ Filter used for the Center model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Center
        fields = ('id', 'name')


class StandFilter(django_filters.FilterSet):
    """ Filter used for the Stand model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Stand
        fields = ('id', 'name')


class ProduceFilter(django_filters.FilterSet):
    """ Filter used for the Produce model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Produce
        fields = ('id', 'name')


class CenterCollection(generics.ListAPIView):
    """
    API endpoint that allows recycling centers to be viewed or edited.
    """
    queryset = models.Center.objects.all()
    serializer_class = serializers.GreenSerializer
    filter_class = MarkerFilter


class StandCollection(generics.ListAPIView):
    """
    API endpoint that allows produce stands to be viewed or edited.
    """
    queryset = models.Stand.objects.all()
    serializer_class = serializers.StandSerializer
    filter_class = StandFilter


class ProduceCollection(generics.ListAPIView):
    """
    API endpoint that allows recycling centers to be viewed or edited.
    """
    queryset = models.Produce.objects.all()
    serializer_class = serializers.ProduceSerializer
    filter_class = ProduceFilter