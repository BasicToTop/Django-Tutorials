from django.urls import path

from .views import home_view, student_create
urlpatterns = [
    path('', home_view, name='home'),
    path('student-create/', student_create, name='student_create'),
]
