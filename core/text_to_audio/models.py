from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PdfModel(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AudioFile(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    pdf = models.ForeignKey(
        PdfModel,on_delete=models.CASCADE,related_name='audio'
        )
    start_page = models.IntegerField()
    end_page = models.IntegerField()
    audio_file = models.FileField(upload_to ='audio/', null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    

