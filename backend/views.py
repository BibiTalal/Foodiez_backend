from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from backend import serializers
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from backend.models import Category, Recipe


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


class Categorylist(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.ListSerializer


class Categorycreate(CreateAPIView):
    serializer_class = serializers.ListSerializer


class Recipelist(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer


class RecipeCreateView(CreateAPIView):
    serializer_class = serializers.RecipeSerializer

    def perform_create(self, serializer):
        serializer.save()


class DeleteRecipeView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.ListSerializer
