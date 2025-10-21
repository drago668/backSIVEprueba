from django.db import models
from .city import City
from .user import User

class Optical(models.Model):
    id_optical = models.AutoField(primary_key=True)
    nameOp = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    city = models.ForeignKey(City, models.DO_NOTHING,db_column='id_city')
    email = models.EmailField(unique=True, max_length=80)
    logo = models.ImageField(upload_to='optical/logos/', null=True, blank=True)
    descriptionOp = models.CharField(max_length=600, default='No hay descripción')
    user = models.ForeignKey(User, models.CASCADE, db_column='id')
    certCadecuacion = models.FileField(upload_to='optical/certCadecuacion/', null=True,blank=True)
    certDispensacion = models.FileField(upload_to='optical/certDispensacion/', null=True ,blank=True)
    latitud = models.FloatField(default=0.0)
    longitud = models.FloatField(default=0.0)
    view = models.PositiveIntegerField(default=0)


    class Meta:
        managed = True
        db_table = 'optical'
