from django.contrib import admin

from .models import *


# Register your models here.

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ['name', 'slug']


admin.site.register(categ, CatAdmin)


class ProdAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'img', 'available']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(product, ProdAdmin)
