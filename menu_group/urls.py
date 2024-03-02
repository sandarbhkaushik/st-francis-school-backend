from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
from .views import ( MenuItemView, GetMenuItem )
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('MenuItem', MenuItemView)
urlpatterns = [
     path('', include(router.urls)),
     path('allmenuitem/', GetMenuItem.as_view()),
]