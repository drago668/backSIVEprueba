from django.db import models
from .answer import Answer

class Recommendation(models.Model):
    id_recommendation = models.AutoField(primary_key=True)
    percentage = models.FloatField
    description = models.CharField(max_length=800)
    total_percentage = models.ForeignKey(Answer, models.DO_NOTHING, db_column='id_answer')
    
    class Meta: 
        managed = True
        db_table = 'recommendation'