from django.urls import path
from mainapp import views
urlpatterns = [
    path('country/', views.country, name='country'),
    path('state/', views.state, name='state'),
]
