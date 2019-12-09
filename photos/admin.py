from django.contrib import admin

# Register your models here.
from .models import Photos


class PhotoAdmin(admin.ModelAdmin):

    list_display = ['title', 'image', 'quant_like', 'created', 'aproved']
    search_fields = ['title', 'author', 'aproved']


admin.site.register(Photos, PhotoAdmin)
