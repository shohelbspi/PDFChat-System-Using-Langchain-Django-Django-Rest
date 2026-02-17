from django.contrib import admin
from chat.models import Pdf,ChatData

# Register your models here.

@admin.register(Pdf)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['id','uuid','file','faiss_path']

@admin.register(ChatData)
class ChatDataAdmin(admin.ModelAdmin):
    list_display=['id','question','answer']