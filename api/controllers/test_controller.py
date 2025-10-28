from api.models import Test
from rest_framework import serializers
from api.serializers import TestSerializers, TestCreateSerializers, TestDeleteSerializers
from api.services import test_service
from rest_framework.response import Response
from rest_framework import generics, status
from permissions import IsOwnerUser, IsAdminUser, IsRegularUser

class TestControllerCreate(generics.GenericAPIView):
    serializer_class = TestSerializers
    queryset = Test.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TestCreateSerializers
        elif self.request.method == 'DELETE':
            return TestDeleteSerializers
        return TestSerializers

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = test_service.TestService()

    permission_classes = [IsRegularUser | IsAdminUser]

    # GET → listar todos los tests
    def get(self, request, *args, **kwargs):
        tests = self.service.list_tests()
        #serializer = self.serializer_class(tests, many=True)
        serializer = self.get_serializer(tests, many=True)
        return Response(serializer.data)
    #permissions_classes = [IsAdminUser| IsRegularUser]
    # POST → crear nuevo test
    def post(self, request, *args, **kwargs):
        # Aquí usamos get_serializer, que instancia el serializer correctamente
        #serializer = self.get_serializer_class(data=request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        try:
            test = self.service.create_test(validated_data)
            # Para devolver la respuesta, también usamos get_serializer
            return Response(self.get_serializer(test).data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        
class TestControllerList(generics.GenericAPIView):
    serializer_class = TestSerializers
    queryset = Test.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = test_service.TestService()
    
    permissions_classes = [IsRegularUser| IsAdminUser]
    # GET → listar por id
    def get(self, request, *args, **kwargs):
        id_test = kwargs.get('pk', None)
        if id_test:
            test = self.service.get_test_by_id(id_test) 
            if not test:
                return Response({"error": "Test no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(test)
            return Response(serializer.data)
    
    permissions_classes = [IsAdminUser]
    # DELETE → eliminar test existente
    def delete(self, request, pk, *args, **kwargs):
        try:
            self.service.delete_test(pk)
            return Response(status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    
