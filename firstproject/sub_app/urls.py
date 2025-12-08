from django.urls import path

from sub_app.views import multiply

urlpatterns = [
    path('multiply/<int:a>/<int:b>/', multiply),  # URL pattern for
    # multiply view
]