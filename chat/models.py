from django.db import models
import uuid

# Create your models here.

class Pdf(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    file = models.FileField(upload_to='pdfs/')
    faiss_path = models.CharField(max_length=500) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self): 
        return str(self.uuid)
    
class ChatData(models.Model):
    pdf = models.ForeignKey(Pdf,on_delete=models.CASCADE,related_name='chats')
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
