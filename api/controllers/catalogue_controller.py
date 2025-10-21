from rest_framework import generics, permissions, status
from rest_framework.response import Response
from permissions import IsOwnerUser, IsAdminUser, IsRegularUser
from api.services import CatalogueService
from api.models import Catalogue
from api.serializers import CatalogueListSerializers, CatalogueCreateSerializers
from drf_spectacular.utils import extend_schema

class CatalogueControllerCreate(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Catalogue.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CatalogueCreateSerializers
        return CatalogueListSerializers

    def __init__(self, **kwargs):
        self.service = CatalogueService()
        super().__init__(**kwargs)
    
    permission_classes = [IsRegularUser , IsAdminUser, IsOwnerUser]
    def get(self, request, *args, **kwargs):
        catalogues = self.service.repository.list()
        serializer = self.get_serializer_class()(catalogues, many=True)
        return Response(serializer.data)

    permission_classes = [IsOwnerUser, IsAdminUser]
    @extend_schema(
        request ={
                'multipart/form-data': {
                'type': 'object',
                'properties': {
                    # Otros campos de texto
                    'nameP': {'type': 'string'},
                    'description': {'type': 'string'},
                    'image': {'type': 'string', 'format': 'binary'},
                    'price': {'type': 'integer'},
                    'optical': {'type': 'integer'},
                }
            }
        }
    )
    # POST → crear nuevo catálogo
    def post(self, request, *args, **kwargs):
      serializer = self.get_serializer_class()(data=request.data)
      if serializer.is_valid():
        validated_data = serializer.validated_data
        try:
          catalogue = self.service.create_catalogue(validated_data)
          return Response(self.get_serializer_class()(catalogue).data, status=status.HTTP_201_CREATED)
        except ValueError as e:
          return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class CatalogueControllerList(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CatalogueListSerializers
    queryset = Catalogue.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CatalogueService()

    permission_classes = [IsRegularUser, IsAdminUser, IsOwnerUser]
    # GET → listar uno por id
    def get(self, request, *args, **kwargs):
        id_catalogue = kwargs.get('pk', None)
        if id_catalogue:
            catalogue = self.service.get_catalogue(id_catalogue)
            if not catalogue:
                return Response({"error": "Catálogo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer_class()(catalogue)
            return Response(serializer.data)
    
    permission_classes = [IsOwnerUser, IsAdminUser]
    @extend_schema(
        request ={
                'multipart/form-data': {
                'type': 'object',
                'properties': {
                    # Otros campos de texto
                    'nameP': {'type': 'string'},
                    'description': {'type': 'string'},
                    'image': {'type': 'string', 'format': 'binary'},
                    'price': {'type': 'integer'},
                    'optical': {'type': 'integer'},
                }
            }
        }
    )
    def patch(self, request, *args, **kwargs):
        id_catalogue = kwargs.get('pk', None)
        if not id_catalogue:
            return Response({"error": "ID de catálogo no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
        
        catalogue = self.service.get_catalogue(id_catalogue)
        if not catalogue:
            return Response({"error": "Catálogo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CatalogueCreateSerializers(data=request.data, partial=True)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            try:
                updated_catalogue = self.service.update_catalogue(catalogue, validated_data)
                return Response(self.get_serializer_class()(updated_catalogue).data)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    permission_classes = [IsOwnerUser, IsAdminUser]
    def delete(self, request, *args, **kwargs):
        id_catalogue = kwargs.get('pk', None)
        if not id_catalogue:
            return Response({"error": "ID de catálogo no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            self.service.delete_catalogue(id_catalogue)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)