from django.db import models
from .day import Day
from .hour import Hour

class Schedule(models.Model): 
    id_schedule = models.AutoField(primary_key=True)
    day = models.ForeignKey(Day, models.DO_NOTHING, db_column='id_day')
    hour_aper = models.ForeignKey(Hour,models.DO_NOTHING, db_column='id_hour_aper', related_name= 'hour_aper')
    hour_close = models.ForeignKey(Hour,models.DO_NOTHING, db_column='id_hour_close', related_name='hour_close')
    
    class Meta: 
        managed = True
        db_table = 'schedule'
