from django.db import models

class Hour(models.Model):
    id_hour= models.AutoField(primary_key=True)
    hour = models.TimeField
    
    class Meta: 
        managed = True
        db_table = 'hour' 