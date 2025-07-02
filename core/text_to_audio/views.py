from django.shortcuts import render
from .serializers import PDFUploadSerializer,AudioConvertSerializer
from django.contrib.auth.models import User
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PdfUploadView(APIView):
    serializer_class = PDFUploadSerializer
    def get(self, request):
        print("Hello world")
        return Response({"message": "Send a POST request to upload a PDF."})
        
    def post(self,request):
        
        serializer = self.serializer_class(
            data = request.data
        )
        
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            )
    




