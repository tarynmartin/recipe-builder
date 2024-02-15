from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    currency = models.CharField(max_length=3, default='USD')
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Recipe(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipes', db_column='user_id')
    recipe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    share_recipe = models.BooleanField(default=False)
    # if linked recipes are not share = true; can't share this recipe; provide feedback about this to user
    linked_recipe_1 = models.ForeignKey('self', on_delete=models.CASCADE, related_name='linked_recipe_A', null=True, blank=True)
    linked_recipe_2 = models.ForeignKey('self', on_delete=models.CASCADE, related_name='linked_recipe_B', null=True, blank=True)
    linked_recipe_3 = models.ForeignKey('self', on_delete=models.CASCADE, related_name='linked_recipe_C', null=True, blank=True)
    linked_recipe_4 = models.ForeignKey('self', on_delete=models.CASCADE, related_name='linked_recipe_D', null=True, blank=True)
    linked_recipe_5 = models.ForeignKey('self', on_delete=models.CASCADE, related_name='linked_recipe_E', null=True, blank=True)

    def __str__(self):
        return self.name

class Ingredients(models.Model):
    # use master list of ingredients for all users
    # any user can add to this list; compare by lower case ingredient name and brand; show as entered by user though; can compare with case insensitivity?
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['ingredient_name', 'brand'], name='uq_ingredient')
        ]

    def __str__(self):
        return self.name
    
class UserIngredients(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ingredients', db_column='user_id')
    ingredient_id = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name='customusers', db_column='ingredient_id')
    amount = models.IntegerField()
    unit = models.CharField(max_length=100)
    date_bought = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user_id', 'ingredient_id'], name='uq_user_ingredient')
        ]

    def __str__(self):
        return self.name
    
# recipe ingredients can show a user what ingredients they need to buy; what do they have on hand?
#  when recipe is completed, update user ingredients amounts; ask user if they want to update ingredient amounts?
class RecipeIngredients(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients', db_column='recipe_id')
    ingredient_id = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name='recipes', db_column='ingredient_id')
    amount = models.IntegerField()
    unit = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class RecipeSteps(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps', db_column='recipe_id')
    step_number = models.IntegerField()
    step_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
