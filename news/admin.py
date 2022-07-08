from django.contrib import admin
from .models import *


class modelAdminNews(admin.ModelAdmin):
    list_display = ('title', 'deleted')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

    def has_delete_permission(self, request, obj=None):
        return False


# Register your models here.
admin.site.register(modelNews, modelAdminNews)