from rest_framework import serializers
from chat.models import Pdf,ChatData

class PDFSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pdf
        fields = "__all__"

class ChatDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatData
        fields = "__all__"
