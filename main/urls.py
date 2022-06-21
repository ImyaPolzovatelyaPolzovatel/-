from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('services', views.services),
    path('news', views.news),
    path('reviews', views.reviews),
    path('contacts', views.contacts),
]
