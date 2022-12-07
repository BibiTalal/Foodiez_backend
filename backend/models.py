from django.db import models


class Ingredient (models.Model):
    ingredient_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ingredient_name


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    # ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, related_name='categories')

    def __str__(self):
        return self.category_name


class Recipe (models.Model):
    food_name = models.CharField(max_length=255)
    recipe = models.TextField()
    # image = models.ImageField(blank=True, null=True)
    description = models.TextField()

    # ingredients = models.ForeignKey(
    #     Ingredient, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(
        Ingredient, related_name='Recipe_ingredients')

    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.food_name
