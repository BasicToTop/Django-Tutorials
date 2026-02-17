from django.urls import path
from .views import login_view, logout_view, user_registration_view

urlpatterns = [ 
    path('login/', login_view, name='login'),
    path('register/', user_registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
