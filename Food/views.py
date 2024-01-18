from rest_framework import viewsets, permissions, status
from .models import UserProfile, SickUserProfile, Food, MealFood
from .serializers import UserProfileSerializer, SickUserProfileSerializer, FoodSerializer, MealFoodSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .permissions import UpdateOwnProfile
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer

    queryset = UserProfile.objects.all()

    @action(detail=True, methods=['get'])
    def calculate_imc(self, request, pk=None):
        user_profile = self.get_object()
        weight = user_profile.weight
        height = user_profile.height

        if (weight and height):
            bmi = weight / (height /100) **2
            #classification en fonction seuil standard
            if(bmi < 18.5):
                classification = 'Sous-poid'
            elif(18.5 <= bmi < 24.9):
                classification = 'Poids normal'
            elif(24.9 <= bmi < 29.9):
                classification = 'Surpoids'
            else:
                classification = 'Obèse'
            return Response({ 'imc' : bmi,  'classification' : classification})
        else:
            return Response({'error ' : 'Weight and Height must be provided for IMC calculation.'}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=True, methods=['get'])
    def predict_health_status(self, request, pk=None):
        """
        Endpoint pour prédire l'état de santé en fonction de l'IMC.
        """
        user_profile = self.get_object()
        weight = user_profile.weight
        height = user_profile.height

        if weight and height:
            # Formule de calcul de l'IMC : poids (kg) / (taille (m) * taille (m))
            bmi = weight / (height / 100) ** 2

            # Classification en fonction des seuils standard de l'IMC
            if bmi < 18.5:
                health_status = 'Sous-poids'
            elif 18.5 <= bmi < 24.9:
                health_status = 'Normal'
            elif 25 <= bmi < 29.9:
                health_status = 'Surpoids'
            else:
                health_status = 'Obèse'

            # Prédiction de l'état de santé en fonction de l'IMC
            if health_status == 'Sous-poids':
                prediction = 'Risque de carence nutritionnelle, consultez un professionnel de la santé.'
            elif health_status == 'Normal':
                prediction = 'Vous semblez être en bonne santé.'
            elif health_status == 'Surpoids':
                prediction = 'Risque accru de maladies liées au poids, considérez une alimentation équilibrée et de l\'exercice.'
            else:
                prediction = 'Risque élevé de maladies liées au poids, consultez un professionnel de la santé.'

            return Response({'imc': bmi, 'health_status': health_status, 'prediction': prediction},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Weight and height must be provided for health prediction.'},
                            status=status.HTTP_400_BAD_REQUEST)




class SickUserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = SickUserProfileSerializer

    queryset = SickUserProfile.objects.all()

class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile, permissions.IsAuthenticated)
    queryset = Food.objects.all()

class MealFoodViewSet(viewsets.ModelViewSet):
    serializer_class = MealFoodSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile, permissions.IsAuthenticated)
    queryset = MealFood.objects.all()

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES