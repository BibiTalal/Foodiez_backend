from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ingredient (models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name


class Recipe (models.Model):
    name = models.CharField(max_length=255)
    recipe = models.TextField()
    # image = models.ImageField(blank=True, null=True)
    # description = models.TextField()

    ingredients = models.ManyToManyField(
        Ingredient, related_name='recipes')
    # ingredients = models.ManyToManyField(
    #     Ingredient, related_name='Recipes')

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='recipes')
    # category = models.ManyToManyField(Category, related_name='recipes')

    def __str__(self):
        return self.name
