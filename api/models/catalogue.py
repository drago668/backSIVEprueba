from django.db import models
from .optical import Optical

class Catalogue(models.Model): 
    id_catalogue = models.AutoField(primary_key=True)
    nameP = models.CharField(max_length=100)
    description = models.TextField
    image = models.CharField(max_length= 300)
    price = models.FloatField
    optical = models.ForeignKey(Optical, models.DO_NOTHING, id_table = 'id_optical')
    
    class Meta: 
        managed = True
        db_table = 'catalogue'