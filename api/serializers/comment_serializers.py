from api.models import Comment
from rest_framework import serializers

class CommentSerializers(serializers.ModelSerializer):
    class Meta: 
        model= Comment
        fields= ['id_comment','descriptionC','user','date_comment','state','score','optical']
        read_only_fields= ['id_comment', 'date_comment']