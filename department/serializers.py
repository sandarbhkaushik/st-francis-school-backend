from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (Department)
from rest_framework import viewsets


class DepartmentReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department

    def create(self, validated_data):
        department = Department(**validated_data)
        department.save()
        return department


