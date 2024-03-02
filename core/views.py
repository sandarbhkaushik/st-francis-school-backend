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
from .models import (CorePage, Media, Event)
from .serializers import (CorePageCreateSerializer,CorePageReadOnlySerializer, EventPageCreateSerializer, EventPageReadOnlySerializer)

class CorePageView(viewsets.ReadOnlyModelViewSet):
    queryset = CorePage.objects.all()
    lookup_field = 'slug'
    serializer_class = CorePageReadOnlySerializer
    serializer_action_classes = {
        'create': CorePageCreateSerializer,
        'list': CorePageReadOnlySerializer,
        'retrieve': CorePageReadOnlySerializer
    }
    class Meta:
        model = CorePage
        fields = '__all__'

class EventPageView(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    lookup_field = 'slug'
    serializer_class = EventPageReadOnlySerializer
    serializer_action_classes = {
        'create': EventPageCreateSerializer,
        'list': EventPageReadOnlySerializer,
        'retrieve': EventPageReadOnlySerializer
    }
    class Meta:
        model = CorePage
        fields = '__all__'

class GetMenuItemChild(APIView):
    serializer_class = CorePageReadOnlySerializer
    def get(self, request, *args, **kwargs):
        menuItemID = self.kwargs['pro']
        menuItemList = list(CorePage.objects.filter(group_id=menuItemID).values('slug','group_id','id','title').order_by('id'))
        return JsonResponse(menuItemList, safe=False)

class GetCorePageDetail(APIView):
    serializer_class = CorePageReadOnlySerializer
    def get(self, request, *args, **kwargs):
        slug_id = self.kwargs['slug']
        corePageDetails = list(CorePage.objects.filter(slug = slug_id).values('slug','group_id','id','title', 'sub_title', 'content').order_by('id'))
        corePageElement = []
        data = []
    
        for f in corePageDetails:
            corePageId = f['id']
            print(corePageId)
            corePageMedia = list(Media.objects.filter(core_page_id = corePageId).values('media_file','id','core_page_id', 'title', 'content').order_by('id'))
            f['media'] = corePageMedia
            data.append(f)

        return JsonResponse(data, safe=False)

class GetCorePageListWithMedia(APIView):
    serializer_class = CorePageReadOnlySerializer
    def get(self, request, *args, **kwargs):
        corePageDetails = list(CorePage.objects.values('slug','group_id','id','title', 'sub_title', 'content').order_by('id'))
        corePageElement = []
        data = []
    
        for f in corePageDetails:
            corePageId = f['id']
            print(corePageId)
            corePageMedia = list(Media.objects.filter(core_page_id = corePageId).values('media_file','id','core_page_id').order_by('id'))
            f['media'] = corePageMedia
            data.append(f)

        return JsonResponse(data, safe=False)