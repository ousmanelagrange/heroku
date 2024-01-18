from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserProfileViewSet, SickUserProfileViewSet, FoodViewSet, MealFoodViewSet, UserLoginApiView


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'sickuserprofiles', SickUserProfileViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'mealfoods', MealFoodViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view()),

]
