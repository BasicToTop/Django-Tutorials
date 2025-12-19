from django.urls import path

from .views import home_view, student_create, student_list
urlpatterns = [
    path('', home_view, name='home'),
    path('student-create/', student_create, name='student_create'),
    path('student-list/', student_list, name='student_list'),
]
