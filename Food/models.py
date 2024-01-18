from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_sick = models.BooleanField(default=False)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    activity_level = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.user.username
    

class SickUserProfile(UserProfile):
    chronic_conditions = models.TextField(null=True, blank=True)
    prescribed_medications = models.TextField(null=True, blank=True)
    # Ajoutez d'autres attributs spécifiques aux utilisateurs malades


class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.FloatField(null=True, blank=True)
    protein_content = models.FloatField(null=True, blank=True)
    carbohydrate_content = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} | calories : {self.calories} | contenance en eau : {self.carbohydrate_content}"



class MealFood(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.FloatField()
    date = models.DateField()
    image = models.ImageField(upload_to='meal_images/', null=True, blank=True)
    grains_quantity = models.FloatField(null=True, blank=True)
    proteins_quantity = models.FloatField(null=True, blank=True)
    dairy_quantity = models.FloatField(null=True, blank=True)
    fruits_quantity = models.FloatField(null=True, blank=True)
    vegetables_quantity = models.FloatField(null=True, blank=True)