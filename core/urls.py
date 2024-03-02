from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
from .views import ( CorePageView, GetCorePageDetail, GetCorePageListWithMedia, EventPageView )
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('CorePage', CorePageView)
router.register('event', EventPageView)
urlpatterns = [
     path('', include(router.urls)),
     # path('menuitemchild/<str:slug>', GetCorePageDetail.as_view()),
     path('corePageDetail/<str:slug>/', GetCorePageDetail.as_view()),
     path('corePageListWithMedia/', GetCorePageListWithMedia.as_view()),

]