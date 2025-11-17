from rest_framework import serializers
from  api.models import * 
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterSerializers(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ('id','email','first_name' ,'last_name','password', 'role_id','is_verified_owner')
        extra_kwargs = {'password': {'write_only':True}}
        read_only_fields = ('role_id', 'id')
        
    def create(self, validated_data):
        if 'username' not in validated_data or not validated_data['username']:
            validated_data['username'] = validated_data['email'].split('@')[0]
            user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
        
    class Meta:
        model= User
        fields =('state')
        reed_only_fields=('state')