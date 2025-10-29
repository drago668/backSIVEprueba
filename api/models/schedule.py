from django.db import models
from .day import Day
from .hour import Hour
from .optical import Optical

class Schedule(models.Model): 
    id_schedule = models.AutoField(primary_key=True)
    optical = models.ForeignKey(Optical, on_delete=models.CASCADE, db_column='id_optical', null=True, blank=True)
    day = models.ForeignKey(Day, on_delete=models.DO_NOTHING, db_column='id_day')
    hour_aper = models.ForeignKey(Hour, on_delete=models.DO_NOTHING, db_column='id_hour_aper', related_name='hour_aper')
    hour_close = models.ForeignKey(Hour, on_delete=models.DO_NOTHING, db_column='id_hour_close', related_name='hour_close')
    class Meta: 
        managed = True
        db_table = 'schedule'
    def __str__(self):
        return f"{self.day} {self.hour_aper} - {self.hour_close}"   
        