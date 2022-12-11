from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/media', null=True)

    def __str__(self):
        return self.name


class Ingredient (models.Model):
    name = models.CharField(max_length=255)
    # cuisine = models.ForeignKey(
    #     Cuisine, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name


class Dish (models.Model):
    name = models.CharField(max_length=255)
    dish = models.TextField()
    image = models.ImageField(upload_to='static/media', null=True)

    ingredients = models.ManyToManyField(
        Ingredient, related_name='dishes')

    cuisine = models.ForeignKey(
        Cuisine, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name
