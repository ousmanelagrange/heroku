from django.contrib import admin
from .models import UserProfile, Food, MealFood, SickUserProfile

admin.site.register(UserProfile)
admin.site.register(Food)
admin.site.register(SickUserProfile)
admin.site.register(MealFood)