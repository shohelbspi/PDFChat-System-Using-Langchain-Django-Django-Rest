from django.urls import path
from chat.views import UploadPdfView,ChatWithPDF,ChatHistory

urlpatterns = [
    path("upload/", UploadPdfView.as_view()),
    path("chat/", ChatWithPDF.as_view()),
    path("history/<uuid:pdf_uuid>/", ChatHistory.as_view()),


 
]
