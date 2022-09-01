from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        an_apiview = [
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,', 
            'sunt in culpa qui officia deserunt mollit anim id est laborum.',
        ]
        return Response({'message' : 'Hello', 'an_apiview' : an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            nama = serializer.validated_data.get('nama')
            email = serializer.validated_data.get('email')
            tgl_lahir = serializer.validated_data.get('tanggal_lahir')

            message = f"Nama saya adalah {nama}. Saya lahir pada tanggal {tgl_lahir}. Email saya adalah {email}"
            return Response({'Pesan' : message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method' : 'put'})

    def patch(self, request, pk=None):
        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):
        return Response({'method' : 'delete'})