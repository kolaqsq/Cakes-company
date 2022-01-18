from django.contrib import admin

from .models import Ingredient, Supplier, CakeDecoration


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'type',)
    list_filter = ('type', 'main_supplier',)
    search_fields = ('code', 'name', 'type', 'desc',)
    ordering = ('code', 'name',)
    autocomplete_fields = ('main_supplier',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'estimated_delivery_time',)
    list_filter = ('estimated_delivery_time',)
    search_fields = ('name', 'estimated_delivery_time', 'address',)


@admin.register(CakeDecoration)
class CakeDecorationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'type',)
    list_filter = ('type', 'main_supplier',)
    search_fields = ('code', 'name', 'type', 'desc',)
    ordering = ('code', 'name',)
    autocomplete_fields = ('main_supplier',)
