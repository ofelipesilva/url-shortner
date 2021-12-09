from django.contrib import admin

from .models import URL

# Register your models here.
@admin.register(URL)
class OriginalURLs(admin.ModelAdmin):
    list_display = ['id', 'link', 'uuid']
