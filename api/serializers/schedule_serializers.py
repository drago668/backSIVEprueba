from api.models import Schedule , Day, Hour, Optical

from rest_framework import serializers

class  DaySerializers(serializers.ModelSerializer):
    class Meta: 
        model = Day
        fields = ['id_day','name_day']

class HourSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Hour
        fields = ['id_hour','hour']
        
        
class ScheduleSerializers(serializers.ModelSerializer):
    day = DaySerializers(read_only=True)
    hour_aper = HourSerializers(read_only=True)
    hour_close = HourSerializers(read_only=True)
    
    day_id = serializers.PrimaryKeyRelatedField(queryset=Day.objects.all(), source='day', write_only=True)
    hour_aper_id = serializers.PrimaryKeyRelatedField(queryset=Hour.objects.all(), source='hour_aper', write_only=True)
    hour_close_id = serializers.PrimaryKeyRelatedField(queryset=Hour.objects.all(), source='hour_close', write_only=True)
    optical_id = serializers.PrimaryKeyRelatedField(queryset=Optical.objects.all(), source='optical', write_only=True)
    class Meta: 
        model = Schedule
        fields = ['id_schedule','day','hour_aper','hour_close', 'day_id','hour_aper_id','hour_close_id', 'optical_id']
        read_only_fields = ['optical', 'day', 'hour_aper', 'hour_close']
        
    