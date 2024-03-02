from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class UserProfileReadOnlySerializer(serializers.ModelSerializer):

    user = UserReadOnlySerializer()

    class Meta:
        model = Profile
        fields = '__all__'
