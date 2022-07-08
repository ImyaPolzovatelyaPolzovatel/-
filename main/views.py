from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from news.models import *
from services.models import *

# Create your views here.
class main(ListView):
    template_name = 'main/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(main, self).get_context_data(**kwargs)
        context.update(
            {
                'news': modelNews.objects.filter(deleted=False).filter(show_on_manepage=True).order_by('-id')[:3],
                'product': modelProduct.objects.filter(deleted=False).filter(show_on_manepage=True).order_by('-id')[:3],
                'footer_news': modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'categories_on_footer': modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'footer_services': modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
            }
        )
        return context

    def get_queryset(self):
        pass


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'

    def get_success_url(self):
        return reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        context.update(
            {
                'footer_news': modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'categories_on_footer': modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'footer_services': modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
            }
        )
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        context.update(
            {
                'footer_news': modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'categories_on_footer': modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'footer_services': modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
            }
        )
        return context

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')