from django.db import models
from .user import User
from .state import State
from .optical import Optical

class Comment(models.Model):
    id_comment = models.AutoField(primary_key=True)
    descriptionC = models.CharField(max_length=500, default='No hay descripcion')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='id')
    date_comment =  models.DateField(auto_now_add=True, null=True, blank=True)
    state =models.ForeignKey(State, models.DO_NOTHING, db_column= 'id_state')
    score = models.IntegerField()
    optical =models.ForeignKey(Optical, models.DO_NOTHING, db_column='id_optical')
    
    class Meta: 
        managed = True
        db_table = 'comment'