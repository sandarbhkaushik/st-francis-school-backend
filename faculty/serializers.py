from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (FacultyProfile)
from rest_framework import viewsets


class FacultyReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyProfile
        fields = '__all__'

class FacultyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyProfile

    def create(self, validated_data):
        facultyProfile = FacultyProfile(**validated_data)
        facultyProfile.save()
        return facultyProfile


