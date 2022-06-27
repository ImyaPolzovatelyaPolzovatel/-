from django.contrib import admin
from .models import *


class modelAdminNews(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    
class modelAdminСategory(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    
class modelAdminAction(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    
class modelAdminProduct(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
# Register your models here.
admin.site.register(modelNews, modelAdminNews)
admin.site.register(modelСategory, modelAdminСategory)
admin.site.register(modelAction, modelAdminAction)
admin.site.register(modelProduct, modelAdminProduct)