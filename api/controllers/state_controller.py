from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.serializers import StateSerializers
from api.models import State

class StateController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StateSerializers
    
    def get(self, request, *args, **kwargs):
        states = State.objects.all()
        serializer = self.serializer_class(states, many=True)
        return Response(serializer.data)

