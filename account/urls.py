from django.urls import path
from .views import *


urlpatterns = [
    path('doctor-login', Signin.as_view(template_name="common_login/login.html"), {'is_doctor': True},
         name="doctor-signin"),
    path('doctor-register', Signup.as_view(
        template_name="doctors/registration.html"), {'is_doctor': True}, name="doctor-signup"),
    path('patient-login',
         Signin.as_view(template_name="common_login/login.html"), {'is_patient': True}, name="patients-signin"),
    path('patient-register', Signup.as_view(
        template_name="patients/registration.html"), {'is_patient': True}, name="patients-signup")
]
