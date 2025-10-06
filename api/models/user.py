from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from .role import Role
from .state import State
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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
  username = models.CharField(max_length=200, null=True, blank=True)
  first_name = models.CharField(max_length=500)
  last_name = models.CharField(max_length=500)
  role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
  state = models.ForeignKey(State,on_delete=models.CASCADE, null=True, blank=True)
  
  objects = UserManager()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  class Meta:
    db_table = 'user'
    managed = True
    
@receiver(reset_password_token_created)
def password_reset_token_created(reset_password_token, *args, **kwargs):
  sitelink = 'http://localhost:3000/'
  token = "?token={}".format(reset_password_token.key)
  full_link = str(sitelink)+str("password_reset")+str(token)
  
  context = {
    'full_link': full_link,
    'email': reset_password_token.user.email
  }
  
  html_message = render_to_string('api/email.html', context=context)
  plain_message = strip_tags(html_message)
  
  msg = EmailMultiAlternatives(
    subject="solicitud de restablecimiento de contraseña para {title}".format(title=reset_password_token.user.email),
    body=plain_message,
    from_email="sivesivebot.2025@gmail.com",
    to=[reset_password_token.user.email]
  )
  
  msg.attach_alternative(html_message, "text/html")
  msg.send()