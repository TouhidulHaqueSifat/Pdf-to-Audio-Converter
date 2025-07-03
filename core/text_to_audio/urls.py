from django.urls import path
from .views import PdfUploadView, ConvertToAudioView
urlpatterns =[
    path('upload-pdf/',PdfUploadView.as_view(), name = 'upload-pdf'),
    path('convert-to-audio/<int:id>/',ConvertToAudioView.as_view(), name = 'convert-to-audio')
]