from django.db import models
from .test import Test
from .question import Question

class Answer(models.Model):
    id_answer = models.AutoField(primary_key=True)
    test = models.ForeignKey(Test, models.DO_NOTHING, db_column='id_test')
    question = models.ForeignKey(Question, models.DO_NOTHING, db_column='id_question')
    total_percentage = models.FloatField
    
    class Meta: 
        managed = True
        db_table = 'answer'
    