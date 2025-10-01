from rest_framework import serializers
from  api.models import * 
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterSerializers(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ('id','email','first_name' ,'last_name','password')
        extra_kwargs = {'password': {'write_only':True}}
        
    #def create(self, validated_data):
     #   if 'username' not in validated_data or not validated_data['username']:
      #      validated_data['username'] = validated_data['email'].split('@')[0]
       # user = User.objects.create_user(**validated_data)
        #return user
    
class LoginSerializers(serializers.ModelSerializer):
    
    class Meta: 
        model = User 
        fields = ('id','email','password')
        extra_kwargs = {'password': {'write_only':True}}
        
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('password', None)
        return ret
        
    