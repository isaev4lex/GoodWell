from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('<slug:lang>', home, name='home'),
]
