from urllib import request

from rest_framework import viewsets
from core import models, serializers, filters
from rest_framework.decorators import action
from django.http import HttpResponse
from core.helpers import get_state_info

from core.params_serializers import ZoneParamsSerializer, CityParamsSerializer, StateByParamsSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    filterset_class = filters.StateFilter
    ordering = ('-id',)

    ordering_fields = '__all__'

    @action(detail=False, methods=['GET'])
    def get_state_by_name(self, request, *args, **kwargs):
        serializer = StateByParamsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        name = data.get('name')
        self.queryset = list(models.State.objects.filter(name__icontains=name). values_list('name', flat=True))
        states = ', '.join(self.queryset)
        response = get_state_info(states)
        return HttpResponse(response, status=200)


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.select_related('state').all()
    serializer_class = serializers.CitySerializer
    filterset_class = filters.CityFilter
    ordering = ('-id',)

    ordering_fields = '__all__'

    @action(detail=False, methods=['GET'])
    def get_city_by_state_name(self, request, *args, **kwargs):
        serializer = CityParamsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.validated_data
        state_name = params.get('state_name')
        self.queryset = self.get_queryset().filter(state__name__iexact=state_name)
        return super(CityViewSet, self).list(request, *args, **kwargs)


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer
    ordering = ('-id',)

    ordering_fields = '__all__'

    @action(detail=False, methods=['GET'])
    def get_zone_by_name(self, request, *args, **kwargs):
        serializer = ZoneParamsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        params = serializer.validated_data
        name = params.get('name')
        self.queryset = self.get_queryset().filter(name__icontains=name)
        return super(ZoneViewSet, self).list(request, *args, **kwargs)


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.select_related('city', 'zone').all()
    serializer_class = serializers.DistrictSerializer
    ordering = ('-id',)

    ordering_fields = '__all__'
