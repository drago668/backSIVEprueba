from rest_framework import generics, permissions
from api.models import User
from api.serializers.user_serializers import RegisterSerializers, LoginSerializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from knox.models import AuthToken

User = get_user_model()

class APIRegister(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializers
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": RegisterSerializers(user).data,
                "token": AuthToken.objects.create(user)[1]
            })
        return Response(serializer.errors, status=400)


class APILogin(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, email=email, password=password)
            if user:
                if User.state == 2:
                    return Response({"error": "Has sido bloqueado por acciones sospechosas comuniquese con el equipo de desarrollo"})
                elif User.state== 4: 
                    return Response(
                        {"error": "Tu cuenta ha sido eliminada."}
                    )
                    
                _, token = AuthToken.objects.create(user)
                return Response({
                    'user': RegisterSerializers(user).data,
                    'token': token
                })
            return Response({'error': 'Invalid credentials'}, status=401)
        return Response(serializer.errors, status=400)
