from django.urls import path, include
from rest_framework import routers
from .views import CheckTCP


urlpatterns = [
    path('tcp', CheckTCP.as_view(), name='tcp'),
    path('tcp/', CheckTCP.as_view(), name='tcp'),
]