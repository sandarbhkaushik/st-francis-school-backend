from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
from .views import ( DepartmentView )
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('Department', DepartmentView)
urlpatterns = [
     path('', include(router.urls)),
]