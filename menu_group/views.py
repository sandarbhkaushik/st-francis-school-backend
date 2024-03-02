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
from .models import MenuItem
from core import models
from .serializers import (MenuItemCreateSerializer, MenuItemReadOnlySerializer)

class MenuItemView(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    lookup_field = 'slug'
    serializer_class = MenuItemReadOnlySerializer
    serializer_action_classes = {
        'create': MenuItemCreateSerializer,
        'list': MenuItemReadOnlySerializer,
        'retrieve': MenuItemReadOnlySerializer
    }
    class Meta:
        model = MenuItem
        fields = '__all__'

class GetMenuItem(APIView):
    serializer_class = MenuItemReadOnlySerializer
    def get(self, request, *args, **kwargs):
        menu = list(MenuItem.objects.values('slug','link','id','title').order_by('id'))
        data = []

        for f in menu:
            childMenuGroupId = f['id']
            menuItemList = list(models.CorePage.objects.filter(group_id=childMenuGroupId).values('slug','group_id','id','title').order_by('id'))
            f['child'] = menuItemList
            data.append(f)

        return JsonResponse(data, safe=False)
