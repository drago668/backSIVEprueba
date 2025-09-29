from django.db import models
from .question import Question

class Option(models.Model):
    id_option = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, models.DO_NOTHING,db_column='id_question')
    correct = models.BinaryField
    
    class Meta: 
        managed = True
        db_table = 'option'