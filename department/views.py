from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
import requests
from django.http import Http404, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from rest_framework import status
from django.contrib.auth.models import User
from .models import Department
from .serializers import (DepartmentCreateSerializer, DepartmentReadOnlySerializer)

class DepartmentView(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    lookup_field = 'slug'
    serializer_class = DepartmentReadOnlySerializer
    serializer_action_classes = {
        'create': DepartmentCreateSerializer,
        'list': DepartmentReadOnlySerializer,
        'retrieve': DepartmentReadOnlySerializer
    }
    class Meta:
        model = Department
        fields = '__all__'

