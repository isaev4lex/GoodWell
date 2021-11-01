from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/', categories, name='categories'),
    path('<slug:slug>/<slug:lang>/', categories, name='categories'),
]
