from django.db import models

class Day(models.Model): 
    id_day = models.AutoField(primary_key=True)
    name_day = models.CharField(max_length=20)
    
    class Meta: 
        managed = True
        db_table = 'day'