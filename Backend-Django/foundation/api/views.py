from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from .models import Contact
from .serializers import ContactSerializer

class ContactView(APIView):
    def post(self, request):
        data_serializer = ContactSerializer(data = request.data)
        if data_serializer.is_valid(raise_exception=True):
            data_serializer.save()
            return Response(data_serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
