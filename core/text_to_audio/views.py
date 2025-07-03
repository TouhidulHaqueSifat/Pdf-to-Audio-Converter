from django.shortcuts import render
from .serializers import PDFUploadSerializer,AudioConvertSerializer
from django.contrib.auth.models import User
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import ExtarctText, ConvertToAudio
import os
from django.conf import settings

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
    

class ConvertToAudioView(APIView):
    serializer_class = AudioConvertSerializer
    extract = ExtarctText
    convert_audio = ConvertToAudio()

    def get_by_id(self, id):
        pdf = PdfModel.objects.get(id = id)
        return pdf
    
    def post(self,request,id):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            #pdf_id = serializer.validated_data['pdf']
            start_page = serializer.validated_data['start_page']
            end_page = serializer.validated_data['end_page']
            try:
                pdf_obj = self.get_by_id(id)
            except PdfModel.DoesNotExist:
                return Response({"error": "PDF not found"}, status=status.HTTP_404_NOT_FOUND)
            pdf = pdf_obj.pdf_file.path
            text = self.extract.extract_text_from_pdf(self, pdf,start_page,end_page)

            audio_filename = f"{pdf_obj.title.replace(' ', '_')}_{start_page}_{end_page}.mp3"

            audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', audio_filename)

            os.makedirs(os.path.dirname(audio_path), exist_ok=True)

            self.convert_audio.convert_to_audio(text,audio_path)

            audio_relative_path = f"audio/{audio_filename}"
            audio_instance = AudioFile.objects.create(
                user=request.user,
                pdf=pdf_obj,
                start_page=start_page,
                end_page=end_page,
                audio_file=audio_relative_path
            )

            return Response({
                "message": "Audio conversion successful",
                "audio_file": request.build_absolute_uri(audio_instance.audio_file.url)
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






