from django.shortcuts import render
from .models import modelNews


# Create your views here.
def main(request):
    _news = modelNews.objects.order_by('-id')[:3]
    return render(request, 'main/main.html', {'news': _news})

    
def services(request):
    return render(request, 'main/services.html')


def news(request):
    _news = modelNews.objects.all()
    return render(request, 'main/news.html', {'news': _news})


def reviews(request):
    return render(request, 'main/reviews.html')


def contacts(request):
    return render(request, 'main/contacts.html')