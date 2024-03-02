from rest_framework.views import APIView
from rest_framework.response import Response
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from .models import Profile

from .serializers import (
    UserProfileReadOnlySerializer
)

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class UserProfileView(APIView):

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = UserProfileReadOnlySerializer(profile)
        return Response(serializer.data)
