from django.urls import path
from .views import home_view, about_view, contact_us_view, login_view, registration_view

urlpatterns = [
    path("", home_view, name="home"),
    path('about/', about_view, name='about'),
    path('contact-us/', contact_us_view, name='contact_us'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
]
