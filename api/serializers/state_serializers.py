from api.models import State
from rest_framework import serializers

class StateSerializers(serializers.ModelSerializer):
    class Meta: 
        model = State
        fields=['id','name'] 