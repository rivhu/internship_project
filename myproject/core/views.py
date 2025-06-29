from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PublicEndpoint(APIView):
    def get(self, request):
        return Response({"message": "This is a public endpoint."})

class ProtectedEndpoint(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {request.user.username}, this is protected."})


# Create your views here.
