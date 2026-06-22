from django_filters import filters, filterset
from core import models
from django.db.models import Q


class CityFilter(filterset.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    id = filters.NumberFilter(lookup_expr='gt')
    nome_do_estado = filters.CharFilter(field_name='state__name', lookup_expr='icontains')

    class Meta:
        model = models.City
        fields = ['name', 'id', 'nome_do_estado']


class StateFilter(filterset.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    abreviacao = filters.CharFilter(lookup_expr='icontains', field_name='abbreviation')
    created_at = filters.DateTimeFromToRangeFilter()
    name_or_abbreviation = filters.CharFilter(method='filter_name_or_abbreviation')
    abbreviation_in = filters.BaseInFilter(field_name='abbreviation')

    @staticmethod
    def filter_name_or_abbreviation(queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(abbreviation__icontains=value))

    class Meta:
        model = models.State
        fields = ['name', 'abreviacao', 'created_at', 'name_or_abbreviation', 'abbreviation_in']
