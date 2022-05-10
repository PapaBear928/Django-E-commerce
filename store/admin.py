from django.contrib import admin

from .models import Categories, Products

admin.site.register(Categories)
admin.site.register(Products)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_by', 'slug', 'description', 'available', 'price', 'on_sale', 'created', 'updated']
	list_filter = ['available', 'on_sale']
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug': ('title',)}
