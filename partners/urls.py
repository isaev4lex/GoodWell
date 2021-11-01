from django.urls import path
from .views import *

urlpatterns = [
    path('', partners, name='partners'),
    path('<slug:lang>', partners, name='partners'),
]
