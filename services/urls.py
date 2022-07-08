from django.urls import path
from .views import *

urlpatterns = [
    path('', services.as_view()),
    path('category/<slug:сategory_slug>/', categoryInfo, name='categoryInfo'),
    path('product/<slug:product_slug>/', productInfo, name='productInfo'),
]

