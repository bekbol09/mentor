from django.contrib import admin

from .models import Ads, Category, Subcategory


admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(Subcategory)

