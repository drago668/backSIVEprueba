from api.models import Test
from rest_framework import serializers
from api.serializers import TestSerializers, TestCreateSerializers, TestDeleteSerializers
from api.services import test_service
from rest_framework.response import Response
from rest_framework import generics, status, permissions


class TestController(generics.GenericAPIView):
    serializer_class = TestSerializers
    create_serializer_class = TestCreateSerializers
    delete_serializer_class = TestDeleteSerializers
    queryset = Test.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = test_service.TestService()

    # GET → listar todas o una por id
    def get(self, request, *args, **kwargs):
        id_test = kwargs.get('pk', None)
        if id_test:
            test = self.service.list_test(id_test) 
            if not test:
                return Response({"error": "Test no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(test)
            return Response(serializer.data)
        else:
            tests = self.service.list_tests()
            serializer = self.serializer_class(tests, many=True)
            return Response(serializer.data)

    # POST → crear nuevo test
    def post(self, request, *args, **kwargs):
        serializer = self.create_serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.data
            try:
                test = self.service.create_test(validated_data)
                return Response(self.create_serializer_class(test).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE → eliminar test existente
    def delete(self, request, pk, *args, **kwargs):
        try:
            self.service.delete_test(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)