from django.urls import path
from api.controllers.user import APILogin, APIRegister

urlpatterns = [
    path("register/", APIRegister.as_view(), name="register"),
    path("login/", APILogin.as_view(), name="login"),
]
