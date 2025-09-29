from django.db import models
from .city import City
from .schedule import Schedule
from .user import User

class Optical(models.Model):
    id_optical = models.AutoField(primary_key=True)
    nameOp = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    city = models.ForeignKey(City, models.DO_NOTHING,db_column='id_city')
    email = models.EmailField(unique=True, max_length=80)
    schedule = models.ForeignKey(Schedule, models.DO_NOTHING, db_column= 'id_schedule')
    logo = models.CharField(max_length=600)
    user = models.ForeignKey(User, models.CASCADE, db_column='id')
    certCadecuacion = models.CharField(max_length=500)
    certDispensacion = models.CharField(max_length=500)
    view = models.IntegerField
    
    class Meta: 
        managed = True
        db_table = 'optical'
    