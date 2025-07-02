from django.urls import path
from .views import PdfUploadView
urlpatterns =[
    path('upload-pdf/',PdfUploadView.as_view(), name = 'upload-pdf')
]