from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import api.controllers as ctrl
from knox import views as knox_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('comment', ctrl.CommentController, basename='comment')
router.register('service', ctrl.ServiceController, basename='service')
router.register('users', ctrl.UsersController, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path("register/", ctrl.APIRegister.as_view(), name="register"),
    path("login/", ctrl.APILogin.as_view(), name="login"),
    path("optical/", ctrl.OpticalControllerCreate.as_view(), name="optical"),
    path("optical/top-viewed/", ctrl.OpticalTopViewedController.as_view(), name="optical_top_viewed"),
    path("optical/by-city/", ctrl.OpticalByCityallController.as_view(), name="optical_by_city"),
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
    path("city/", ctrl.CityController.as_view(), name = "city"),
    path("state/",ctrl.StateController.as_view(), name = "estado"),
    path("optical/report/",ctrl.createReport.as_view(), name = 'optical-report-pdf'),
    path('product/',ctrl.ProductController.as_view(), name= 'Product'),
    path('admin/pending-owners/', ctrl.admin_controller.pending_optics, name='get_pending_optic_owners'),
    path('admin/approve-owner/<int:optic_id>/', ctrl.admin_controller.approve_optic_owner, name='approve_optic_owner'),
    path('admin/reject-owner/<int:optic_id>/', ctrl.admin_controller.reject_optic_owner, name='reject_optic_owner'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
