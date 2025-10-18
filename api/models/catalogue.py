from django.db import models
from .optical import Optical

class Catalogue(models.Model): 
    id_catalogue = models.AutoField(primary_key=True)
    nameP = models.CharField(max_length=100)
    description = models.CharField(max_length=500 , default='Sin descripción')
    image = models.CharField(max_length= 300)
    price = models.IntegerField( default=0)
    optical = models.ForeignKey(Optical, models.DO_NOTHING, db_column = 'id_optical')
    
    class Meta: 
        managed = True
        db_table = 'catalogue'
