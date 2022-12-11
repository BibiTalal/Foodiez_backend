
from rest_framework import generics
from backend import serializers
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
# from rest_framework.decorators import api_view

from .models import Cuisine, Dish, Ingredient


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


class Cuisinelist(ListAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = serializers.CuisineSerializer


class Cuisinecreate(CreateAPIView):
    serializer_class = serializers.CuisineSerializer

# The Recipe Crud ..


class CuisineUpdateView(UpdateAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = serializers.CuisineUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cuisine_id'


class DeleteCuisineView(DestroyAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = serializers.CuisineSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cuisine_id'


class Dishlist(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = serializers.DishSerializer


class DishCreateView(CreateAPIView):
    serializer_class = serializers.DishSerializer

    def perform_create(self, serializer):
        serializer.save()


class DishUpdateView(UpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = serializers.DishUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'dish_id'


class DeleteDishView(DestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = serializers.DishSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'dish_id'


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
    lookup_url_kwarg = 'ingrediant_id'


class DeleteIngrediantView(DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ingrediant_id'
