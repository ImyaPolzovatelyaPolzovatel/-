from django.urls import path
from .views import *

urlpatterns = [
    path('', news.as_view()),
    path('filter/', NewsFilter, name="NewsFilter"),
    path('<slug:post_slug>/', newsInfo.as_view(), name="newsInfo"),

]

