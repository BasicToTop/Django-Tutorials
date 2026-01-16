from django.urls import path
from mainapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('country/', views.country, name='country'),
    path('country_list/', views.country_list, name='country_list'),
    path('state/', views.state, name='state'),
    path('qualification/', views.qualification, name='qualification'),
    path('gender/', views.gender, name='gender'),
    path('university/', views.university, name='university'),
    path('student/', views.student, name='student'),
]
