from api.models import Optical, City
from rest_framework import serializers

class OpticalCreateSerializers(serializers.ModelSerializer):
  def validate(self, data):
        print("LOGO =>", data.get("logo"))
        return data
  class Meta:
    model = Optical
    fields = ['id_optical', 'descriptionOp','nameOp', 'address', 'tel', 'city', 'email', 'logo', 'certCadecuacion', 'certDispensacion', 'latitud', 'longitud', 'is_verified']
    read_only_fields = ['id_optical', 'is_verified']

class OpticalListSerializers(serializers.ModelSerializer):
  class Meta:
    model = Optical
    fields = ['id_optical', 'descriptionOp', 'nameOp', 'address', 'tel', 'city', 'email', 'logo', 'user', 'certCadecuacion', 'certDispensacion', 'latitud', 'longitud', 'view']
    read_only_fields = ['id_optical', 'view', 'user']

class OpticalTopViewedSerializers(serializers.Serializer):
  nameOp = serializers.CharField(max_length=255)
  view = serializers.IntegerField()

class OpticalByAllCitySerializers(serializers.Serializer):
  city_name = serializers.CharField(max_length=255)
  count = serializers.IntegerField()

class CitySerializers(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ['id_city', 'name']
