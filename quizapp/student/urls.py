from django.urls import path
from . import views
from . import studentviews

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login', studentviews.student_loginpage, name='loginpage'),
    path('student_register', studentviews.student_registrationpage, name='registration')

]
