from django.contrib import admin

from .models import Category, Property, Media

admin.site.register(Category)
admin.site.register(Property)
admin.site.register(Media)