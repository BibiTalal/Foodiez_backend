from django.contrib import admin
from .models import Recipe, Ingredient, Category
# Register your models here.

MyModels = [Recipe, Ingredient, Category]
admin.site.register(MyModels)
