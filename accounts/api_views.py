from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Profile
from .serializers import ProfileSerializer

class ProfileListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
