from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (MenuItem)
from rest_framework import viewsets


class MenuItemReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class MenuItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem

    def create(self, validated_data):
        menuItem = MenuItem(**validated_data)
        menuItem.save()
        return menuItem


