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
from .models import FacultyProfile
from .serializers import (FacultyCreateSerializer, FacultyReadOnlySerializer)

class FacultyView(viewsets.ReadOnlyModelViewSet):
    queryset = FacultyProfile.objects.all()
    lookup_field = 'slug'
    serializer_class = FacultyReadOnlySerializer
    serializer_action_classes = {
        'create': FacultyCreateSerializer,
        'list': FacultyReadOnlySerializer,
        'retrieve': FacultyReadOnlySerializer
    }
    class Meta:
        model = FacultyProfile
        fields = '__all__'

class GetProfileByDepartment(APIView):
    serializer_class = FacultyReadOnlySerializer
    def get(self, request, *args, **kwargs):
        slugId = self.kwargs['slug']
        departmentList = list(FacultyProfile.objects.filter(slug=slugId).values('slug','first_name','last_name', 'contact_number','email','profile_image','department' ).order_by('id'))
        return JsonResponse(departmentList, safe=False)