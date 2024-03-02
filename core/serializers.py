from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (CorePage, Event, Media)
from rest_framework import viewsets

class MediaReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class CorePageReadOnlySerializer(serializers.ModelSerializer):
    media = MediaReadOnlySerializer(many=True, read_only=True)
    
    class Meta:
        model = CorePage
        fields = '__all__'

class CorePageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorePage
        exclude = ('slug')
    def create(self, validated_data):
        corePage = CorePage(**validated_data)
        corePage.save()
        return corePage


class EventPageReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventPageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('slug')
    def create(self, validated_data):
        corePage = CorePage(**validated_data)
        corePage.save()
        return corePage
