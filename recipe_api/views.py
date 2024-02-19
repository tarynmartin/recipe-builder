from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PATCH'])
def user(request, email):
    if request.method == 'GET':
        user = CustomUser.objects.filter(email=email)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        user = CustomUser.objects.get(user_id=request.data['user_id'])
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_recipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def recipe(request, recipe_id):
    if request.method == 'GET':
        recipe = Recipe.objects.get(recipe_id=recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        recipe = Recipe.objects.get(recipe_id=recipe_id)
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recipe = Recipe.objects.get(recipe_id=recipe_id)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def ingredients(request):
    if request.method == 'GET':
        ingredients = Ingredients.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_ingredients(request, user_id):
    if request.method == 'GET':
        user_ingredients = UserIngredients.objects.filter(user_id=user_id)
        serializer = UserIngredientSerializer(user_ingredients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserIngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def user_ingredient(request, user_id, ingredient_id):
    if request.method == 'GET':
        user_ingredient = UserIngredients.objects.get(user_id=user_id, ingredient_id=ingredient_id)
        serializer = UserIngredientSerializer(user_ingredient)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        user_ingredient = UserIngredients.objects.get(user_id=user_id, ingredient_id=ingredient_id)
        serializer = UserIngredientSerializer(user_ingredient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user_ingredient = UserIngredients.objects.get(user_id=user_id, ingredient_id=ingredient_id)
        user_ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                 

@api_view(['GET'])
def recipe_ingredients(request, recipe_id):
    recipe_ingredients = RecipeIngredients.objects.filter(recipe_id=recipe_id)
    serializer = RecipeIngredientSerializer(recipe_ingredients, many=True)
    return Response(serializer.data)

@api_view(['POST', 'PATCH', 'DELETE'])
def recipe_ingredient(request):
    if request.method == 'POST':
        serializer = RecipeIngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        recipe_ingredient = RecipeIngredients.objects.get(recipe_id=request.data['recipe_id'], ingredient_id=request.data['ingredient_id'])
        serializer = RecipeIngredientSerializer(recipe_ingredient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recipe_ingredient = RecipeIngredients.objects.get(recipe_id=request.data['recipe_id'], ingredient_id=request.data['ingredient_id'])
        recipe_ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def recipe_steps(request, recipe_id):
    recipe_steps = RecipeSteps.objects.filter(recipe_id=recipe_id)
    serializer = StepSerializer(recipe_steps, many=True)
    return Response(serializer.data)

@api_view(['POST', 'PATCH', 'DELETE'])
def recipe_step(request):
    if request.method == 'POST':
        serializer = StepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        recipe_step = RecipeSteps.objects.get(recipe_id=request.data['recipe_id'], step_number=request.data['step_number'])
        serializer = StepSerializer(recipe_step, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recipe_step = RecipeSteps.objects.get(recipe_id=request.data['recipe_id'], step_number=request.data['step_number'])
        recipe_step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)