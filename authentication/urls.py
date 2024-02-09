from django.urls import path
from .views import RegisterView, VerificationView, UsernameValidationView, EmailValidationView, LoginView
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    # path('', views.start, name='start'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('validate-username/', csrf_exempt(UsernameValidationView.as_view()),
         name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate_email'),
    path('activate/<uidb64>/<token>',
         VerificationView.as_view(), name='activate'),


]
