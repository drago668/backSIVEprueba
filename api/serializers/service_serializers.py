from api.models import Service
from rest_framework import serializers

class ServiceSerializers(serializers.ModelSerializer):
    class Meta: 
        model= Service
        fields= ['id_service','name_service','optical']
        read_only_fields = ['id_service']