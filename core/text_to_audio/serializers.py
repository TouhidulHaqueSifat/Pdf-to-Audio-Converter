from rest_framework import serializers
from .models import *

class PDFUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfModel
        fields = '__all__'

class AudioConvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioFile
        fields = ['pdf','start_page','end_page']