from api.models import Questionary, Question, Option
from rest_framework import serializers

class QuestionaryCreateSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Questionary
        fields = ['name_questionary', 'description', 'Author']

class QuestionaryListSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Questionary
        fields = ['id_questionary', 'name_questionary', 'description', 'Author']
        read_only_fields = ['id_questionary']
        
class QuestionCreateSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Question
        fields = ['question', 'image_question', 'questionary']

class OptionCreateSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Option
        fields = ['descriptionOp', 'question']

class OptionListSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Option
        fields = ['id_option', 'descriptionOp', 'question']
        read_only_fields = ['id_option']
        
class QuestionListSerializers(serializers.ModelSerializer):
    options = OptionListSerializers(many=True, read_only=True)
    
    class Meta: 
        model = Question
        fields = ['id_question', 'question', 'image_question', 'questionary', 'options']
        read_only_fields = ['id_question']


