from django.urls import path
from testapp.views import test
urlpatterns = [
    # Define your URL patterns here
    path('test/', test, name='test'),
]
