from rest_framework import generics,status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.serializers import CommentSerializers
from api.models import Comment

class CommentController(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated]
    
    http_method_names = ['get','post','patch','delete']
