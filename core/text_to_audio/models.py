from django.db import models

# Create your models here.

class PdfModel(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)

class AudioFile(models.Model):
    pdf = models.ForeignKey(
        PdfModel,on_delete=models.CASCADE,related_name='audio'
        )
    start_page = models.IntegerField()
    end_page = models.IntegerField()
    audio_file = models.FileField(upload_to ='audio/', null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    

