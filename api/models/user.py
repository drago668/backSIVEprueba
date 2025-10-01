from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from .role import Role
from .state import State

class UserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields ):
    if not email:
      raise ValueError('Falta el correo electronico')

    email = self.normalize_email(email)
    user = self.model(email = email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
  email = models.EmailField(max_length=200, unique=True)
  first_name = models.CharField(max_length=500)
  last_name = models.CharField(max_length=500)
  role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
  state = models.ForeignKey(State,on_delete=models.CASCADE, null=True, blank=True)
  
  objects = UserManager()
  

  REQUIRED_FIELDS = []
  class Meta:
    db_table = 'user'
    managed = True