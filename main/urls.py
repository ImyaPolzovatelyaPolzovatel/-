from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('services/', views.services),
    path('services/category/<slug:сategory_slug>/', views.categoryInfo, name='categoryInfo'),
    path('services/product/<slug:product_slug>/', views.productInfo, name='productInfo'),
    path('news/', views.news),
    path('news/<slug:post_slug>/', views.newsInfo, name='newsInfo'),
    path('reviews/', views.reviews),
    path('contacts/', views.contacts),
    
]

