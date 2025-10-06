from rest_framework import generics, status, permissions
from rest_framework.response import Response
from api.services import OpticalService
from api.models import Optical, Day, Hour, Schedule
from api.serializers import OpticalListSerializers, OpticalCreateSerializers
from api.serializers import DaySerializers
from api.serializers import HourSerializers
from api.serializers import ScheduleSerializers
from django.db.models import F
class OpticalController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    create_serializer_class = OpticalCreateSerializers
    list_serializer_class = OpticalListSerializers
    queryset = Optical.objects.all()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = OpticalService() 
        
    def get_serializer_class(self):
        if self.action == 'create':
            return OpticalCreateSerializers
        return OpticalListSerializers

    # GET → listar todas o una por id
    def get(self, request, *args, **kwargs):
        id_optical = kwargs.get('pk', None)
        if id_optical:
            optical = self.service.repository.get_optical_by_id(id_optical)
            if not optical:
                return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.list_serializer_class(optical)
            return Response(serializer.data)
        else:
            opticals = self.service.list_optical()
            serializer = self.list_serializer_class(opticals, many=True)
            return Response(serializer.data)

    # POST → crear nueva óptica
    def post(self, request, *args, **kwargs):
        serializer = self.create_serializer_class(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data['user'] = request.user
            try:
                optical = self.service.create_optical(validated_data)
                return Response(self.create_serializer_class(optical).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT → actualizar óptica existente
    def patch(self, request, pk, *args, **kwargs):
        try:
            optical = self.service.repository.get_optical_by_id(pk)
            if not optical:
                return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Optical.DoesNotExist:
            return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.list_serializer_class(optical, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                optical = self.service.update_optical(pk, serializer.validated_data)
                return Response(self.list_serializer_class(optical).data)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE → eliminar óptica
    def delete(self, request, pk, *args, **kwargs):
        try:
            deleted = self.service.delete_optical(pk)
            if deleted:
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class OpticalIncrementViewController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, pk):
        try:
            optical = Optical.objects.get(pk=pk)
            optical.views = F('views') + 1
            optical.save(update_fields=['views'])
            optical.refresh_from_db()
            serializer = OpticalListSerializers(optical)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Optical.DoesNotExist:
            return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
class DayController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DaySerializers
    queryset = Day.objects.all()
    
    def get(self, request, *args, **kwargs):
        days = Day.objects.all()
        serializer = DaySerializers(days, many=True)
        return Response(serializer.data)
    
class HourController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = HourSerializers
    queryset = Hour.objects.all()
    
    def get(self, request, *args, **kwargs):
        hours = Hour.objects.all()
        serializer = HourSerializers(hours, many=True)
        return Response(serializer.data)

class ScheduleController(generics.GenericAPIView):
    #permission_classes = [permissions.AllowAny]
    serializer_class = ScheduleSerializers
    queryset = Schedule.objects.all()
    
   # 🔹 GET → Listar todos o uno por id
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            try:
                schedule = Schedule.objects.get(pk=pk)
                serializer = ScheduleSerializers(schedule)
                return Response(serializer.data)
            except Schedule.DoesNotExist:
                return Response({'error': 'Horario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        else:
            schedules = Schedule.objects.all()
            serializer = ScheduleSerializers(schedules, many=True)
            return Response(serializer.data)

    # 🔹 POST → Crear nuevo horario
    def post(self, request, *args, **kwargs):
        serializer = ScheduleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    # 🔹 DELETE → Eliminar horario
    def delete(self, request, pk, *args, **kwargs):
        try:
            schedule = Schedule.objects.get(pk=pk)
            schedule.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Schedule.DoesNotExist:
            return Response({'error': 'Horario no encontrado'}, status=status.HTTP_404_NOT_FOUND)