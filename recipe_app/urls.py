"""
URL configuration for recipe_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from recipe_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', views.user),
    path('api/recipes/', views.recipes),
    path('api/recipe/', views.create_recipe),
    path('api/recipe/<int:recipe_id>/', views.recipe),
    path('api/ingredients/', views.ingredients_list),
    path('api/user_ingredients/', views.user_ingredients),
    path('api/user_ingredient/<int:user_ingredient_id>/', views.user_ingredient),
    path('api/recipe_ingredients/', views.recipe_ingredients),
    path('api/recipe_ingredient/', views.recipe_ingredient),
    path('api/recipe_steps/', views.recipe_steps),
    path('api/recipe_step/', views.recipe_step),
]
