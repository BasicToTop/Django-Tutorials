from django.urls import path
from mainapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('country/', views.country, name='country'),
    path('country_list/', views.country_list, name='country_list'),
    path('country-delete/<int:pk>/', views.country_delete, name='country_delete'),
    path('country-detail/<int:pk>/', views.country_detail, name='country_detail'),
    path('country-edit/<int:pk>/', views.country_edit, name='country_edit'),
    path('state/', views.state, name='state'),
    path('qualification/', views.qualification, name='qualification'),
    path('gender/', views.gender, name='gender'),
    path('university/', views.university, name='university'),
    path('student/', views.student, name='student'),
]
