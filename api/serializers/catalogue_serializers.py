from api.models import Catalogue
from rest_framework import serializers

class CatalogueCreateSerializers(serializers.ModelSerializer):
  class Meta:
    model = Catalogue
    fields = ['optical','nameP', 'description', 'price','image']

class CatalogueListSerializers(serializers.ModelSerializer):
  class Meta:
    model = Catalogue
    fields = ['id_catalogue', 'nameP', 'description', 'price', 'image']
    read_only_fields = ['id_catalogue']