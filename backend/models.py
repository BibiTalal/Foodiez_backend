from django.db import models


class Ingredient (models.Model):
    ingredient_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ingredient_name


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    ingredient = models.ManyToManyField(Ingredient, related_name='ingredient')

    def __str__(self):
        return self.category_name


class Recipe (models.Model):
    food_name = models.CharField(max_length=255)
    recipe = models.TextField()
    # image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    ingredient = models.ManyToManyField(
        Ingredient, related_name='Recipe_ingredient')
    category = models.ManyToManyField(Category, related_name='category')

    def __str__(self):
        return self.food_name
