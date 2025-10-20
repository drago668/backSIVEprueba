from django.db import models
from .questionary import Questionary
from .option import Option
from .question import Question
from .user import User

class Test (models.Model):
  id_test = models.AutoField(primary_key=True)
  questionary = models.ForeignKey(Questionary, models.DO_NOTHING, db_column='id_questionary')
  question= models.ForeignKey(Question, models.DO_NOTHING, db_column='id_question',default=0)
  user= models.ForeignKey(User, models.DO_NOTHING, db_column='id')
  date_test = models.DateField(auto_now_add=True)
  source = models.ForeignKey(Option,models.DO_NOTHING, db_column= 'source')
  
  class Meta: 
    db_table = 'test'
    managed = True