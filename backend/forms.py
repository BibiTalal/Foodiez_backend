# from .models import Recipe, Ingredient, Category
# from django import forms
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class IngredientForm(forms.ModelForm):
#     class Meta:
#         model = Ingredient
#         fields = ['ingredient_name']


# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['category_name']


# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['food_name', 'recipe', 'category', 'ingredient']


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             "password": forms.PasswordInput(),
#         }


# class SigninForm(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput())
#     access = forms.CharField(required=True)
