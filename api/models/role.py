from django.db import models

class Role(models.Model):
  name = models.CharField(max_length=20)
  def __str__(self):
    return self.name
  class Meta:
    db_table = 'role'
    managed = True
  