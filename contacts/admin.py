from .models import *
from django.contrib import admin


# Register your models here.
class AdminContacts(admin.ModelAdmin):
    list_display = ("name", "email")


admin.site.register(Contacts, AdminContacts)
