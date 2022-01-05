from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):

        an_apiview = [
            "Test 123",
            "Test 321",
            "Test 213",
        ]

        return Response({"Message" : "Halo Dunia", "APIView" : an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            msg = f"Hello {name}"
            return Response({
                "Message" : msg,
                "Email" : serializer.validated_data.get("email")}
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({"Method" : "PUT"})

    def patch(self, request, pk=None):
        return Response({"Method" : "Patch"})

    def delete(self, request, pk=None):
        return Response({"Method" : "Delete"})

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({"Message" : "Hello", "a_viewset" : a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            msg = f"Hello {name}"
            return Response({
                "Message" : msg,
                "Email" : serializer.validated_data.get("email")}
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
