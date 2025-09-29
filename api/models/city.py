from django.db import models

class City(models.Model):
    id_city = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    class Meta: 
        managed = True
        db_table = 'city'