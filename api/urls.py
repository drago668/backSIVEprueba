from django.urls import path 
from rest_framework.routers import DefaultRouter
from api.controllers import *
from api.controllers.user import LoginViewset, RegisterViewset

router = DefaultRouter()
router.register('register', RegisterViewset, basename='register')
router.register('login', LoginViewset, basename='login')
urlpatterns = router.urls