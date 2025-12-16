from django.urls import path
from mainapp.views import home, about, table_view, form_view
urlpatterns = [
    # Define your URL patterns here
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('table/', table_view, name='table'),
    path('form/', form_view, name='form')
]
