from django.db import models

class Recommendation(models.Model):
    id_recommendation = models.AutoField(primary_key=True)
    percentage = models.FloatField
    description = models.CharField(max_length=800)

    
    class Meta: 
        managed = True
        db_table = 'recommendation'