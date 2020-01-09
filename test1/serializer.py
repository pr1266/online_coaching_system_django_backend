from .models import *
from rest_framework.serializers import ModelSerializer , SerializerMethodField , CharField , ValidationError , StringRelatedField, PrimaryKeyRelatedField
from django.db.models import Q


class ContractSerializer(ModelSerializer):

    class Meta:
        model  = Contract
        fields = '__all__'

class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

class AthleteSerializer(ModelSerializer):

    class Meta:
        model = Athlete
        fields = '__all__'

class CoachSerializer(ModelSerializer):

    class Meta:
        model = Coach
        fields = '__all__'

class CitySerializer(ModelSerializer):

    class Meta:
        model =  City
        fields = '__all__'