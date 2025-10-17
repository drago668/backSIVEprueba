from django.db import models
from .question import Question

class Option(models.Model):
    id_option = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, models.DO_NOTHING,db_column='id_question', related_name='options')
    descriptionOp = models.CharField(max_length=500, default='Sin descripción')
    correct = models.BooleanField(default=False)
    
    class Meta: 
        managed = True
        db_table = 'option'