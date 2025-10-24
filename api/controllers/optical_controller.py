from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response
from permissions import IsOwnerUser, IsAdminUser, IsRegularUser
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from api.services import OpticalService
from api.models import Optical, Day, Hour, Schedule, Service, City
from api.serializers import CitySerializers
from api.serializers import OpticalListSerializers, OpticalCreateSerializers, OpticalTopViewedSerializers, OpticalByAllCitySerializers
from api.serializers import DaySerializers
from api.serializers import HourSerializers
from api.serializers import ScheduleSerializers, ServiceSerializers
from django.db.models import F
from drf_spectacular.utils import extend_schema, OpenApiTypes
class OpticalControllerCreate(generics.GenericAPIView):
    
    def get_queryset(self):
        return Optical.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsAdminUser | IsOwnerUser]
        elif self.request.method == 'GET':
            permission_classes = [IsRegularUser | IsOwnerUser | IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def __init__(self, **kwargs):
        self.service = OpticalService()
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        optics = self.service.repository.list()
        serializer = self.get_serializer_class()(optics, many=True)
        return Response(serializer.data)


    parser_classes = (MultiPartParser, FormParser, JSONParser)
    @extend_schema(
        # Sobrescribe el esquema para la carga de archivos
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    # Otros campos de texto
                    'nameOp': {'type': 'string'},
                    'address': {'type': 'string'},
                    'tel': {'type': 'string'},
                    'city': {'type': 'integer'},
                    'email': {'type': 'string', 'format': 'email'},
                    'certCadecuacion': {'type': 'string', 'format': 'binary'},
                    'certDispensacion': {'type': 'string', 'format': 'binary'},
                    'latitud': {'type': 'number', 'format': 'float'},
                    'longitud': {'type': 'number', 'format': 'float'},

                    # 💥 Esto fuerza el campo 'logo' a ser un selector de archivos
                    'logo': {'type': 'string', 'format': 'binary'},

                    # ... (otros campos de texto)
                }
            }
        },
        responses={201: OpticalListSerializers}
    )
    # POST → crear nueva óptica
    def post(self, request, *args, **kwargs):
      serializer = self.get_serializer_class()(data=request.data)
      if serializer.is_valid():
        validated_data = serializer.validated_data
        validated_data['user'] = request.user
        try:
          optical = self.service.create_optical(validated_data)
          return Response(self.get_serializer_class()(optical).data, status=status.HTTP_201_CREATED)
        except ValueError as e:
          return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OpticalControllerList(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpticalListSerializers
    queryset = Optical.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = OpticalService()
    
    def get_permissions(self):
        if self.request.method == 'PATCH':
            permission_classes = [IsAdminUser | IsOwnerUser]
        elif self.request.method == 'DELETE':
            permission_classes = [IsAdminUser | IsOwnerUser]
        elif self.request.method == 'GET':
            permission_classes = [IsRegularUser | IsOwnerUser | IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    # GET → listar una por id
    def get(self, request, *args, **kwargs):
        id_optical = kwargs.get('pk', None)
        if id_optical:
            optical = self.service.get_optical(id_optical)
            if not optical:
              return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
            optical.view = F('view') + 1
            optical.save(update_fields=['view'])
            optical.refresh_from_db()
            serializer = self.serializer_class(optical)
            return Response(serializer.data)

    @extend_schema(
        # Sobrescribe el esquema para la carga de archivos
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    # Otros campos de texto
                    'nameOp': {'type': 'string'},
                    'address': {'type': 'string'},
                    'tel': {'type': 'string'},
                    'city': {'type': 'integer'},
                    'email': {'type': 'string', 'format': 'email'},
                    'certCadecuacion': {'type': 'string', 'format': 'binary'},
                    'certDispensacion': {'type': 'string', 'format': 'binary'},
                    'latitud': {'type': 'number', 'format': 'float'},
                    'longitud': {'type': 'number', 'format': 'float'},

                    # 💥 Esto fuerza el campo 'logo' a ser un selector de archivos
                    'logo': {'type': 'string', 'format': 'binary'},

                    # ... (otros campos de texto)
                }
            }
        },
        responses={201: OpticalListSerializers}
    )
    # PUT → actualizar óptica existente
    def patch(self, request, pk, *args, **kwargs):
        try:
            optical = self.service.repository.get_optical_by_id(pk)
            if not optical:
                return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Optical.DoesNotExist:
            return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(optical, data=request.data, partial=True)
        if serializer.is_valid():
            if 'logo' in serializer.validated_data and optical.logo:
                optical.logo.delete(save=False)
            try:
                optical_updated = self.service.update_optical(optical, serializer.validated_data)
                return Response(self.serializer_class(optical_updated).data)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE → eliminar óptica
    def delete(self, request, pk, *args, **kwargs):

        try:
            deleted = self.service.delete_optical(pk)
            if deleted:
                return Response(status=status.HTTP_200_OK)
            return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class OpticalTopViewedController(generics.GenericAPIView):
    permission_classes = [IsAdminUser| IsOwnerUser]
    serializer_class = OpticalTopViewedSerializers

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = OpticalService()

    def get(self, request, *args, **kwargs):
        top_viewed_optics = self.service.get_top_viewed_opticals()
        serializer = self.serializer_class(top_viewed_optics, many=True)
        return Response(serializer.data)

class OpticalByCityallController(generics.GenericAPIView):
    permission_classes = [IsAdminUser| IsOwnerUser]
    serializer_class = OpticalByAllCitySerializers

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = OpticalService()

    def get(self, request, *args, **kwargs):
        # traer todas las ópticas de todas las ciudades
        city_data = self.service.get_city_distribution_data()
        serializer = self.serializer_class(city_data, many=True)
        return Response(serializer.data)
class CityController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class= CitySerializers

    def get(self,request, *args, **kwargs):
        cities = City.objects.all()
        serializer = self.serializer_class(cities, many=True)
        return Response(serializer.data)

class DayController(generics.GenericAPIView):
    serializer_class = DaySerializers
    queryset = Day.objects.all()

    permission_classes = [IsOwnerUser| IsAdminUser]
    def get(self, request, *args, **kwargs):
        days = Day.objects.all()
        serializer = DaySerializers(days, many=True)
        return Response(serializer.data)

class HourController(generics.GenericAPIView):
    permission_classes = [IsOwnerUser| IsAdminUser]
    serializer_class = HourSerializers
    queryset = Hour.objects.all()

    def get(self, request, *args, **kwargs):
        hours = Hour.objects.all()
        serializer = HourSerializers(hours, many=True)
        return Response(serializer.data)

class ScheduleControllerCreate(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ScheduleSerializers
    queryset = Schedule.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ScheduleSerializers
        return ScheduleSerializers

    permissions_classes = [IsOwnerUser|IsAdminUser]
   # 🔹 GET → Listar todos
    def get(self, request, *args, **kwargs):
      schedules = Schedule.objects.all()
      serializer = ScheduleSerializers(schedules, many=True)
      return Response(serializer.data)

    permissions_classes = [IsOwnerUser| IsAdminUser]
    # 🔹 POST → Crear nuevo horario
    def post(self, request, *args, **kwargs):
        serializer = ScheduleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScheduleControllerList(generics.GenericAPIView):
    serializer_class = ScheduleSerializers

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ScheduleSerializers
        elif self.request.method == 'DELETE':
            return ScheduleSerializers
        return ScheduleSerializers

    permission_classes = [IsOwnerUser| IsAdminUser]
    def get(self, request, *args, **kwargs):
        id_schedule = kwargs.get('pk', None)
        if id_schedule:
            try:
                schedule = Schedule.objects.get(pk=id_schedule)
            except Schedule.DoesNotExist:
                return Response({'error': 'Horario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ScheduleSerializers(schedule)
            return Response(serializer.data)

    permission_classes = [IsOwnerUser| IsAdminUser]
    # 🔹 PUT → Actualizar horario existente
    def put(self, request, pk, *args, **kwargs):
        try:
            schedule = Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            return Response({'error': 'Horario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ScheduleSerializers(schedule, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [IsOwnerUser| IsAdminUser]
    # 🔹 DELETE → Eliminar horario
    def delete(self, request, pk, *args, **kwargs):
        try:
            schedule = Schedule.objects.get(pk=pk)
            schedule.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Schedule.DoesNotExist:
            return Response({'error': 'Horario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class ServiceController(viewsets.ModelViewSet):
        queryset = Service.objects.all()
        serializer_class= ServiceSerializers
        http_method_names=['get','post','patch','delete']
