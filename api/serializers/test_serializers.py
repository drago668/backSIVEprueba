from api.models import Test, Questionary, User
from rest_framework import serializers

class TestSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Test
        fields = ['id_test', 'questionary', 'user', 'date_test', 'answer' ]

class TestCreateSerializers(serializers.ModelSerializer):
    # questionary_id = serializers.PrimaryKeyRelatedField(queryset=Questionary.objects.all())
    # user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    questionary_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    question_id= serializers.IntegerField()
   # answer_id= serializers.IntegerField()
    class Meta: 
        model = Test
        fields = ['id_test', 'questionary_id', 'question_id', 'user_id', 'date_test']
        read_only_fields = ['id_test']
        
class TestDeleteSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Test
        fields = ['id_test']