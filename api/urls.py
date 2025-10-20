from django.urls import path, include
import api.controllers as ctrl
from knox import views as knox_views

urlpatterns = [
    path("register/", ctrl.APIRegister.as_view(), name="register"),
    path("login/", ctrl.APILogin.as_view(), name="login"),
    path("optical/", ctrl.OpticalControllerCreate.as_view(), name="optical"),
    path("optical/<int:pk>/", ctrl.OpticalControllerList.as_view(), name="optical_detail"),
    path("days/", ctrl.DayController.as_view(), name="days"),
    path("hours/", ctrl.HourController.as_view(), name="hours"),
    path("schedules/", ctrl.ScheduleControllerCreate.as_view(), name="schedules"),
    path("schedules/<int:pk>/", ctrl.ScheduleControllerList.as_view(), name="schedule_detail"),
    path('questionary/',ctrl.QuestionaryControllerCreate.as_view(), name='questionary'),
    path('questionary/<int:pk>/',ctrl.QuestionaryControllerList.as_view(), name='questionary_detail'),
    path('question/',ctrl.QuestionControllerCreate.as_view(), name='question'),
    path('question/<int:pk>/',ctrl.QuestionControllerList.as_view(), name='question_detail'),
    path('option/',ctrl.OptionControllerCreate.as_view(), name='option'),
    path('option/<int:pk>/',ctrl.OptionControllerList.as_view(), name='option_detail'),
    path('logout/',knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/',knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('password_reset/',include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('test/',ctrl.TestControllerCreate.as_view(), name='test'),
    path('test/<int:pk>/',ctrl.TestControllerList.as_view(), name='test_detail'),
    path('catalogue/', ctrl.CatalogueControllerCreate.as_view(), name='catalogue'),
    path('catalogue/<int:pk>/', ctrl.CatalogueControllerList.as_view(), name='catalogue_detail'),
    path("city/", ctrl.CityController.as_view(), name = "citys"),
    path("state/",ctrl.StateController.as_view(), name = "estado")
]
