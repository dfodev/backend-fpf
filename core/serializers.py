from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from core import models


class StateSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.State
        fields = '__all__'


class CitySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'

        expandable_fields = {
            'state': ('core.StateSerializer', {'fields': ['id', 'name', 'abbreviation']}),
        }


class ZoneSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Zone
        fields = '__all__'


class DistrictSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'
