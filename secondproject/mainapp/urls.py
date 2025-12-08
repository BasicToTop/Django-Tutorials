from django.urls import path
from mainapp.views import home, about
urlpatterns = [
    # Define your URL patterns here
    path('', home, name='home'),
    path('about/', about, name='about'),
]
