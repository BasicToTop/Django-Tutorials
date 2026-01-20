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
    path('state_list/', views.state_list, name='state_list'),
    path('state-delete/<int:pk>/', views.state_delete, name='state_delete'),
    path('state-detail/<int:pk>/', views.state_detail, name='state_detail'),
    path('state-edit/<int:pk>/', views.state_edit, name='state_edit'),

    path('qualification/', views.qualification, name='qualification'),
    path('qualification_list/', views.qualification_list,
         name='qualification_list'),
    path('qualification-delete/<int:pk>/',
         views.qualification_delete, name='qualification_delete'),
    path('qualification-detail/<int:pk>/',
         views.qualification_detail, name='qualification_detail'),
    path('qualification-edit/<int:pk>/',
         views.qualification_edit, name='qualification_edit'),

    path('gender/', views.gender, name='gender'),
    path('gender_list/', views.gender_list, name='gender_list'),
    path('gender-delete/<int:pk>/', views.gender_delete, name='gender_delete'),
    path('gender-detail/<int:pk>/', views.gender_detail, name='gender_detail'),
    path('gender-edit/<int:pk>/', views.gender_edit, name='gender_edit'),

    path('university/', views.university, name='university'),
    path('university_list/', views.university_list, name='university_list'),
    path('university-delete/<str:pk>/',
         views.university_delete, name='university_delete'),
    path('university-detail/<str:pk>/',
         views.university_detail, name='university_detail'),
    path('university-edit/<str:pk>/',
         views.university_edit, name='university_edit'),

    path('university/', views.university, name='university'),
    path('university_list/', views.university_list, name='university_list'),
    path('university-delete/<int:pk>/',
         views.university_delete, name='university_delete'),
    path('university-detail/<int:pk>/',
         views.university_detail, name='university_detail'),
    path('university-edit/<int:pk>/',
         views.university_edit, name='university_edit'),

    path('student/', views.student, name='student'),
    path('student_list/', views.student_list, name='student_list'),
    path('student-delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('student-detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('student-edit/<int:pk>/', views.student_edit, name='student_edit'),

]
