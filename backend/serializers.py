from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from backend.models import Cuisine, Ingredient, Dish
User = get_user_model()

# Authentications Serializers ..


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "access", "username", "password"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        payload = RefreshToken.for_user(new_user)
        token = str(payload.access_token)

        validated_data["access"] = token
        # print("Successfully Created An Acount with FOODIEZ")

        return validated_data


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        print(data)
        username = data.get("username")
        password = data.get("password")

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            raise serializers.ValidationError("User Does Not Exist!!")
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect Password")

        payload = RefreshToken.for_user(user)
        payload["username"] = user.username
        token = str(payload.access_token)
        data["username"] = user.username

        data["access"] = token
        return data

# Category Serializer ..


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['id', 'name', 'image']


class CuisineUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['name',  'image']

# Recipes Serializer ..


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'cuisine', 'ingredients', 'image']


class DishUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['name', 'ingredients', 'cuisine', 'image']

# Ingredient Serializer ..


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class IngrediantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']
