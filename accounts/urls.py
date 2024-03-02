from django.urls import path, include
from .views import (
    GoogleLogin,
    UserProfileView
)

urlpatterns = [
    path('google/login/', GoogleLogin.as_view()),
    path('me/', UserProfileView.as_view())
]
