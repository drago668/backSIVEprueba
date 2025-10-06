from django.urls import path, include
from api.controllers.user import APILogin, APIRegister
from api.controllers.optical import OpticalController, DayController, HourController, ScheduleController, OpticalIncrementViewController
from knox import views as knox_views

urlpatterns = [
    path("register/", APIRegister.as_view(), name="register"),
    path("login/", APILogin.as_view(), name="login"),
    path("optical/", OpticalController.as_view(), name="optical"),
    path("optical/<int:pk>/", OpticalController.as_view(), name="optical_detail"),
    path("optical/<int:pk>/increment_view/", OpticalIncrementViewController.as_view(), name="optical_increment_view"),
    path("days/", DayController.as_view(), name="days"),
    path("hours/", HourController.as_view(), name="hours"),
    path("schedules/", ScheduleController.as_view(), name="schedules"),
    path("schedules/<int:pk>/", ScheduleController.as_view(), name="schedule_detail"),
    path('logout/',knox_views.LogoutView.as_view(), name='knox_logout'), 
    path('logoutall/',knox_views.LogoutAllView.as_view(), name='knox_logoutall'), 
    path('password_reset/',include('django_rest_passwordreset.urls', namespace='password_reset')), 
]
