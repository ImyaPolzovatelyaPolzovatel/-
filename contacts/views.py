from news.models import *
from services.models import *
from django.views.generic import CreateView
from .forms import *
from .service import send


# Create your views here.
#почту отправлять селари
#изменить функции для выводы на классы
#флейк 8, для подсвтеки ошибок в оформлении
class contacts(CreateView):
    model = Contacts
    form_class = ContactsForm
    template_name = 'contacts/contacts.html'
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(contacts, self).get_context_data(**kwargs)
        context.update(
            {
                'footer_news': modelNews.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'categories_on_footer': modelСategory.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id'),
                'footer_services': modelProduct.objects.filter(deleted=False).filter(show_on_footer=True).order_by('-id')
            }
        )
        return context

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)