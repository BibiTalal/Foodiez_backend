
from rest_framework import generics
from backend import serializers
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.decorators import api_view

from .models import Category, Recipe, Ingredient


class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer


class SigninView(APIView):
    serializer_class = serializers.SigninSerializer

    def post(self, request):
        data = request.data
        serializer = serializers.SigninSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# The Category Crud ..


class Categorylist(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class Categorycreate(CreateAPIView):
    serializer_class = serializers.CategorySerializer

# The Recipe Crud ..


class Recipelist(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer


class RecipeCreateView(CreateAPIView):
    serializer_class = serializers.RecipeSerializer

    def perform_create(self, serializer):
        serializer.save()


class RecipeUpdateView(UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeUpdateSerializer
    lookup_field = 'id'
    # lookup_url_kwarg = 'recipe_id'

    def update(recipe_id, request):
        recipe = Recipe.objects.get(id=recipe_id)
        serializer = Recipelist.get_serializer(request.POST, instance=Recipe)
        if request.method == "POST":
            if serializer.is_valid():
                serializer.save()
                return ("update succefully")
            else:
                return Response("failed")


# class RecipeUpdateView(UpdateAPIView):
#     @api_view(['POST'])
#     def update(request, id):
#         item = Recipe.objects.get(id=id)
#         data = serializers.RecipeUpdateSerializer(
#             instance=item, data=request.data)


class DeleteRecipeView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    lookup_field = 'id'
    # queryset = Recipe.objects.all()
    # serializer_class = serializers.RecipeSerializer
    # lookup_field = 'id'
    # lookup_url_kwarg = 'recipe_id'

    def DeleteRecipe(request, recipe_id):
        Recipe.objects.get(id=recipe_id)
        return ("Done you deleated one recipe!!")


# The ingredients Crud ..

class IngrediantList(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class IngrediantCreateView(CreateAPIView):
    serializer_class = serializers.IngredientSerializer

    def perform_create(self, serializer):
        serializer.save()


class IngrediantUpdateView(UpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngrediantUpdateSerializer
    lookup_field = 'id'

    def update(ingrediant_id, request):
        recipe = Ingredient.objects.get(id=ingrediant_id)
        serializer = IngrediantList.get_serializer(
            request.POST, instance=Ingredient)
        if request.method == "POST":
            if serializer.is_valid():
                serializer.save()
                return ("update succefully")
            else:
                return Response("failed")


class DeleteIngrediantView(DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
    lookup_field = 'id'

    def DeleteIngrediant(request, ingrediant_id):
        Recipe.objects.get(id=ingrediant_id).delete()
        return ("Done you deleated one recipe!!")
