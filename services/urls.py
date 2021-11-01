from django.urls import path
from .views import *

urlpatterns = [
    path('', services, name='services'),
    path('<slug:lang>', services, name='services'),
]
