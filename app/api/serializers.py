from .models import Data

from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = (
            'id',
            'url',
            'processed',
            'error',
        )
        read_only_fields = ('processed', 'error',)


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = (
            'id',
            'url',
            'keys',
        )
        read_only_fields = ('id', 'url', 'keys',)
