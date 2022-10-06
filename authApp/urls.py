from rest_framework import routers
from django.urls import path
from .views import ConductorView



urlpatterns = [
    path('conductor/',ConductorView.as_view(), name='conductor_view'),
    path('conductor/<int:pk>',ConductorView.as_view(), name='conductor_view')

]
    
