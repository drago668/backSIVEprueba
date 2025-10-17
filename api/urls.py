from django.urls import path, include
import api.controllers as ctrl
from knox import views as knox_views

urlpatterns = [
    path("register/", ctrl.APIRegister.as_view(), name="register"),
    path("login/", ctrl.APILogin.as_view(), name="login"),
    path("optical/", ctrl.OpticalController.as_view(), name="optical"),
    path("optical/<int:pk>/", ctrl.OpticalController.as_view(), name="optical_detail"),
    path("optical/<int:pk>/increment_view/", ctrl.OpticalIncrementViewController.as_view(), name="optical_increment_view"),
    path("days/", ctrl.DayController.as_view(), name="days"),
    path("hours/", ctrl.HourController.as_view(), name="hours"),
    path("schedules/", ctrl.ScheduleController.as_view(), name="schedules"),
    path("schedules/<int:pk>/", ctrl.ScheduleController.as_view(), name="schedule_detail"),
    path('questionary/',ctrl.QuestionaryController.as_view(), name='questionary'),
    path('questionary/<int:pk>/',ctrl.QuestionaryController.as_view(), name='questionary_detail'), 
    path('question/',ctrl.QuestionController.as_view(), name='question'),
    path('question/<int:pk>/',ctrl.QuestionController.as_view(), name='question_detail'), 
    path('option/',ctrl.OptionController.as_view(), name='option'),
    path('option/<int:pk>/',ctrl.OptionController.as_view(), name='option_detail'),
    path('logout/',knox_views.LogoutView.as_view(), name='knox_logout'), 
    path('logoutall/',knox_views.LogoutAllView.as_view(), name='knox_logoutall'), 
    path('password_reset/',include('django_rest_passwordreset.urls', namespace='password_reset')),
    path ('test/',ctrl.TestController.as_view(), name='test'),
    path ('test/<int:pk>/',ctrl.TestController.as_view(), name='test_detail'), 
]
