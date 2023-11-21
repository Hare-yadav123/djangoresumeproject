from django.urls import path 
from .import views

urlpatterns = [
    path('ser/' ,views.service),
]
