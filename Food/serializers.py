from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, SickUserProfile, Food, MealFood

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data.get('username', '')
        )

        return user
    def update(self, instance, validated_data):
        """Update and return an existing user"""
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        # Utilisez set_password pour mettre à jour le mot de passe correctement
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'

class SickUserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SickUserProfile
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class MealFoodSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    food = FoodSerializer()

    class Meta:
        model = MealFood
        fields = '__all__'
