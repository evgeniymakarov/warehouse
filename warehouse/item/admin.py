from django.contrib import admin

from item.models import Item, Category, Warehouse, Position, Units

# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Warehouse)
admin.site.register(Position)
admin.site.register(Units)