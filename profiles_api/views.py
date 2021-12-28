from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


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
