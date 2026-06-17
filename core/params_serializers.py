from rest_framework import serializers


class ZoneParamsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class CityParamsSerializer(serializers.Serializer):
    state_name = serializers.CharField(required=True)
