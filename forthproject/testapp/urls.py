from django.urls import path

from .views import home_view, student_create, student_list, student_delete
urlpatterns = [
    path('', home_view, name='home'),
    path('student-create/', student_create, name='student_create'),
    path('student-list/', student_list, name='student_list'),
    path('student-delete/<int:record_id>/', student_delete, name='student_delete'),
]
