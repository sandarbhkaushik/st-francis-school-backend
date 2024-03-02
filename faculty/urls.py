from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
from .views import ( FacultyView, GetProfileByDepartment )
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('Faculty', FacultyView)
urlpatterns = [
     path('', include(router.urls)),
     path('profilebydepartment/<str:slug>', GetProfileByDepartment.as_view()),

]