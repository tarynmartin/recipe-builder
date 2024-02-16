from rest_framework import serializers
from .models import Recipe, Ingredients, RecipeSteps, CustomUser, UserIngredients, RecipeIngredients

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('user_id', 'email', 'password', 'currency')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
# I don't want to create a user here, I want to get the user
    # def create(self, validated_data):
    #     user = CustomUser.objects.create_user(
    #         email=validated_data['email'],
    #         password=validated_data['password']
    #     )
    #     return user

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('recipe_id', 'user_id', 'name', 'created_at', 'updated_at', 'share_recipe', 'linked_recipe_1', 'linked_recipe_2', 'linked_recipe_3', 'linked_recipe_4', 'linked_recipe_5')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('ingredient_id', 'ingredient_name', 'brand')

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeSteps
        fields = ('id', 'recipe_id', 'step_number', 'description')

class UserIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIngredients
        fields = ('user_id', 'ingredient_id', 'amount', 'unit', 'date_bought', 'expiration_date', 'created_at', 'updated_at')

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredients
        fields = ('recipe_id', 'ingredient_id', 'amount', 'unit', 'created_at', 'updated_at')

