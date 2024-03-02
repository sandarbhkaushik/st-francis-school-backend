"""power_bi_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (path, include)
from rest_auth.views import UserDetailsView, LogoutView
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
schema_view = get_swagger_view(title='Power BI Dashboard API')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('accounts.urls')),
    path('auth/logout/', LogoutView.as_view()),
    path('accounts/', include('allauth.urls')),
    path('core/', include('core.urls')),
    path('menu/', include('menu_group.urls')),
    path('department/', include('department.urls')),
    path('faculty/', include('faculty.urls')),
    path('swagger/', schema_view),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)