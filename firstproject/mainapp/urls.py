from django.urls import path

from mainapp.views import home_view, about_view, sum

urlpatterns = [

    path('home/', home_view),  # Added URL pattern for home_view
    path('about/', about_view),  # Added URL pattern for about_view
    path('sum/<int:a>/<int:b>/', sum),  # URL pattern for sum view
]
