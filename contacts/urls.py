from django.urls import path, include
from .views import *

urlpatterns = [
    path('', contacts.as_view()),

]