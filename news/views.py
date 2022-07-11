from django.shortcuts import render, get_object_or_404
from .models import *
from services.models import *
from django.views.generic import ListView, DetailView

# Create your views here.
class news(ListView):
    #from django.http import JsonResponse
    #ajax метод post
    #джанга фильтрс
    template_name = 'news/news.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(news, self).get_context_data(**kwargs)
        context.update(
            {
                'news': modelNews.objects.filter(deleted=False).order_by('-id'),
                'footer_news': modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'categories_on_footer': modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'footer_services': modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
            }
        )
        return context

    def get_queryset(self):
        pass


class newsInfo(DetailView):
    model = modelNews
    template_name = 'news/newsInfo.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(newsInfo, self).get_context_data(**kwargs)
        context.update(
            {
                'footer_news': modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'categories_on_footer': modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'footer_services': modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
            }
        )
        return context


def NewsFilter(request):
    if request.method == "GET":
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date and end_date:
            _news = modelNews.objects.filter(time_create__range=[start_date, end_date]).order_by('-id')
        else:
            _news = []
    else:
        _news = modelNews.objects.all()

    footer_news = modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    categories_on_footer = modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    footer_services = modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    return render(request, 'news/news.html', {
                                                'news': _news,
                                                'footer_news': footer_news,
                                                'categories_on_footer': categories_on_footer,
                                                'footer_services': footer_services
                                             })

