from django.shortcuts import render
from chat.serializers import PDFSerializer,ChatDataSerializer
from chat.models import Pdf,ChatData
from chat.service import process_pdf,ask_question
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser,FormParser
import os


# Create your views here.

class UploadPdfView(APIView):

    parser_classes = [MultiPartParser,FormParser]

    def post(self, request):

        file = request.FILES.get("file")

        if not file:
            return Response({"error": "No file uploaded"})


        pdf = Pdf.objects.create(file=file)

        faiss_path = f"faiss_indexes/{pdf.uuid}"

        os.makedirs(faiss_path, exist_ok=True)

        process_pdf(pdf.file.path, faiss_path)

        pdf.faiss_path = faiss_path

        pdf.save()

        return Response({

            "pdf_uuid": str(pdf.uuid)

        })

class ChatWithPDF(APIView):

    def post(self, request):

        question = request.data.get("question")

        pdf_uuid = request.data.get("pdf_uuid")

        pdf = Pdf.objects.get(uuid=pdf_uuid)

        answer = ask_question(question, pdf.faiss_path)

        ChatData.objects.create(

            pdf=pdf,
            question=question,
            answer=answer

        )

        return Response({

            "answer": answer

        })
    
class ChatHistory(APIView):

    def get(self, request, pdf_uuid):

        pdf = Pdf.objects.get(uuid=pdf_uuid)

        chats = pdf.chats.all().order_by("created_at")

        serializer = ChatDataSerializer(chats, many=True)

        return Response(serializer.data)