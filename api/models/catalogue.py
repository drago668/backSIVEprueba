from django.db import models
from .optical import Optical
from .product import Product

class Catalogue(models.Model): 
    id_catalogue = models.AutoField(primary_key=True)
    nameP = models.ForeignKey(Product, models.DO_NOTHING, db_column='id_product')
    description = models.CharField(max_length=500 , default='Sin descripción')
    image = models.ImageField(upload_to='catalogue/image/', null=True, blank=True)
    price = models.IntegerField( default=0)
    optical = models.ForeignKey(Optical, models.CASCADE, db_column = 'id_optical')
    
    class Meta: 
        managed = True
        db_table = 'catalogue'
