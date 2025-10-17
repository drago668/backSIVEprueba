from django.db import models
from .questionary import Questionary
from .user import User

class Test (models.Model):
  id_test = models.AutoField(primary_key=True)
  questionary = models.ForeignKey(Questionary, models.DO_NOTHING, db_column='id_questionary')
  user= models.ForeignKey(User, models.DO_NOTHING, db_column='id')
  date_test = models.DateField(auto_now_add=True)
  source = models.CharField(max_length=500)
  
  class Meta: 
    db_table = 'test'
    managed = True