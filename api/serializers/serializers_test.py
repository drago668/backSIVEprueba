from api.models import Test
from rest_framework import serializers

class TestSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Test
        fields = ['id_test', 'questionary', 'user', 'date_test', 'source' ]

class TestCreateSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Test
        fields = ['id_test', 'questionary', 'user', 'date_test', 'source']
        read_only_fields = ['id_test' ]
        
class TestDeleteSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Test
        fields = ['id_test']