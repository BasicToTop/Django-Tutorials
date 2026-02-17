from django.urls import path

from mainapp import views
urlpatterns = [
    path('register/', views.user_registration, name='user_registration'),
    path('login/', views.login_view, name='login'),
    path('', views.dashboard_view, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about_view, name='about'),
]
