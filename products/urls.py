from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/', product, name='product'),
    path('<slug:slug>/<slug:lang>/', product, name='product'),
]
