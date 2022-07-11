from django.shortcuts import render, redirect
from .models import *
from .forms import *
from news.models import *
from services.models import *
from django.views.generic import ListView


# Create your views here.
def reviews(request):
    if request.method == 'POST':
        form = AddReview(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

    else:
        form = AddReview()
    _reviews = review.objects.filter(deleted=False).filter(moderation=False).filter(published=True).order_by('-id')
    footer_news = modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    categories_on_footer = modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    footer_services = modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    return render(request, 'reviews/reviews.html', {'form': form, 'review': _reviews, 'footer_news': footer_news, 'categories_on_footer': categories_on_footer, 'footer_services': footer_services})