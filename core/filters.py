from django_filters import filters, filterset
from core import models

class CityFilter(filterset.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.City
        fields = ['name']