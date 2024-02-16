from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *

# create a view for the user
# create a delete function for admin? is that built into the admin board?
@api_view(['GET', 'POST', 'PATCH'])
def user(request):
    if request.method == 'GET':
        user = CustomUser.objects.filter(email=request.data['email'], password=request.data['password'])
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

#create a view for all recipes
@api_view(['GET'])
def recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

#create a view for a recipe               
@api_view(['POST'])
def create_recipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def recipe(request):
    if request.method == 'GET':
        recipe = Recipe.objects.get(recipe_id=request.data['recipe_id'])
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        recipe = Recipe.objects.get(recipe_id=request.data['recipe_id'])
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recipe = Recipe.objects.get(recipe_id=request.data['recipe_id'])
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# create an ingredient
# get all ingredients

# USER INGREDIENTS
# get all ingredients

# create an ingredient
# get an ingredient
# update an ingredient - patch
# delete an ingredient

# RECIPE INGREDIENTS
# get all recipe ingredients

# create a recipe ingredient
# update a recipe ingredient - patch
# delete a recipe ingredient

# RECIPE STEPS
# get all recipe steps

# create a recipe step
# update a recipe step - patch
# delete a recipe step