from django.contrib import admin
from .models import Author, Food, Unit, Recipe, Ingredient

admin.site.register(Food)
admin.site.register(Author)
admin.site.register(Unit)
admin.site.register(Recipe)
admin.site.register(Ingredient)
