from django.urls import path
from .views import *

urlpatterns = [
    path('', contacts, name='contacts'),
    path('<slug:lang>', contacts, name='contacts'),
]
