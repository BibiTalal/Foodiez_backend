from django.contrib import admin
from backend.models import Cuisine, Ingredient, Dish
# Register your models here.

MyModels = [Cuisine, Dish, Ingredient]
admin.site.register(MyModels)
