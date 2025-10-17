from django.db import models
from .questionary import Questionary

class Question (models.Model): 
    id_question = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    image_question = models.CharField(max_length= 500)
    questionary = models.ForeignKey(Questionary, models.DO_NOTHING, db_column='id_questionary', related_name='questions')
    
    class Meta: 
        managed = True
        db_table = 'question'
    