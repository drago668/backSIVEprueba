from api.models import Optical, City
from rest_framework import serializers

class OpticalCreateSerializers(serializers.ModelSerializer):
  class Meta:
    model = Optical
    fields = ['nameOp', 'address', 'tel', 'city', 'email', 'logo', 'certCadecuacion', 'certDispensacion', 'latitud', 'longitud']

class OpticalListSerializers(serializers.ModelSerializer):
  class Meta:
    model = Optical
    fields = ['id_optical', 'nameOp', 'address', 'tel', 'city', 'email', 'logo', 'user', 'certCadecuacion', 'certDispensacion', 'latitud', 'longitud', 'view']
    read_only_fields = ['id_optical', 'view', 'user']
    
class CitySerializers(serializers.ModelSerializer):
  class Meta: 
    model = City 
    fields = ['id_city', 'name']