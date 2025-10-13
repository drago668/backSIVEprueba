from django.db import models

class Questionary(models.Model):
    id_questionary = models.AutoField(primary_key=True)
    name_questionary = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    Author = models.CharField(max_length=100)
    date = models.DateField
    
    class Meta: 
        managed = True
        db_table = 'questionary'