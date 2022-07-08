from django.shortcuts import render, get_object_or_404
from .models import *
from news.models import *
from django.views.generic import ListView, DetailView

# Create your views here.
class services(ListView):
    template_name = 'services/services.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(services, self).get_context_data(**kwargs)
        context.update(
            {
                'category': modelСategory.objects.all(),
                'action': modelAction.objects.filter(deleted=False),
                'product': modelProduct.objects.filter(deleted=False).order_by('-id')[:5],
                'footer_news': modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'categories_on_footer': modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'footer_services': modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
            }
        )
        return context

    def get_queryset(self):
        pass


def categoryInfo(request, сategory_slug):
    _category = get_object_or_404(modelСategory, slug=сategory_slug)
    footer_news = modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    categories_on_footer = modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    footer_services = modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    _categoryInfo = []
    while _category.parent != None:
        _category = _category.parent
        _categoryInfo.insert(0, _category)
    _category = get_object_or_404(modelСategory, slug=сategory_slug)
    _categoryInfo.append(_category)
    _product = modelСategory.objects.get(name=_category).prod.filter(deleted=False)
    return render(request, 'services/categoryInfo.html', {'category': _category, 'categoryInfo': _categoryInfo, 'product': _product, 'footer_news': footer_news, 'categories_on_footer': categories_on_footer, 'footer_services': footer_services})


def productInfo(request, product_slug):
    _product = get_object_or_404(modelProduct, slug=product_slug)
    _category = modelСategory.objects.filter(prod__id=_product.id)
    _action = modelProduct.objects.get(title=_product).act.filter(deleted=False)
    footer_news = modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    categories_on_footer = modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    footer_services = modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
    return render(request, 'services/productInfo.html', {'product': _product, 'category': _category, 'action': _action, 'footer_news': footer_news, 'categories_on_footer': categories_on_footer, 'footer_services': footer_services})
