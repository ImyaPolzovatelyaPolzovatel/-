from django.contrib import admin
from .models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'time_create', 'published', 'moderation', 'deleted')

    def has_delete_permission(self, request, obj=None):
        return False


# Register your models here.
admin.site.register(review, ReviewAdmin)
