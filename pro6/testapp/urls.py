from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contact, name='contact'),
]
