from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, requset, format = None):

        an_apiview = [
            "Test 123",
            "Test 321",
            "Test 213",
        ]

        return Response({"Message" : "Halo Dunia", "APIView" : an_apiview})
