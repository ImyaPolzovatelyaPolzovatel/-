from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import *


class modelAdminСategory(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def has_delete_permission(self, request, obj=None):
        return False


class modelAdminAction(admin.ModelAdmin):
    list_display = ('title', 'deleted')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

    def has_delete_permission(self, request, obj=None):
        return False

class modelAdminProduct(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def get_model_perms(self, request):
        return {}

    def has_delete_permission(self, request, obj=None):
        return False

# Register your models here.

admin.site.register(modelСategory, modelAdminСategory)
admin.site.register(modelAction, modelAdminAction)
admin.site.register(modelProduct, modelAdminProduct)