from django.db import models
from .optical import Optical

class Service(models.Model):
    id_service = models.AutoField(primary_key=True)
    name_service = models.CharField(max_length=300)
    optical = models.ForeignKey(Optical, models.DO_NOTHING, db_column = 'id_optical')
    
    class Meta: 
        managed = True
        db_table = 'service'