from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def main(request):
    _news = modelNews.objects.order_by('-id')[:3]
    return render(request, 'main/main.html', {'news': _news})

    
def services(request):
    _category = modelСategory.objects.all()
    _action = modelAction.objects.all()
    _product = modelProduct.objects.all()
    return render(request, 'main/services.html', {'category': _category, 'action': _action, 'product': _product})


def categoryInfo(request, сategory_slug):
    _category = get_object_or_404(modelСategory, slug=сategory_slug)
    return render(request, 'main/categoryInfo.html', {'category': _category})


def productInfo(request, product_slug):
    _product = get_object_or_404(modelProduct, slug=product_slug)
    return render(request, 'main/productInfo.html', {'product': _product})


def news(request):
    _news = modelNews.objects.all()
    #start_date = request.GET.get('start_date')
    #end_date = request.GET.get('end_date')
    #print(start_date)
    return render(request, 'main/news.html', {'news': _news})


def newsInfo(request, post_slug):
    _news = get_object_or_404(modelNews, slug=post_slug)
    return render(request, 'main/newsInfo.html', {'news': _news})


def reviews(request):
    return render(request, 'main/reviews.html')


def contacts(request):
    return render(request, 'main/contacts.html')