from .models import *
from rest_framework.serializers import ModelSerializer , SerializerMethodField , CharField , ValidationError , StringRelatedField, PrimaryKeyRelatedField
from django.db.models import Q


class ContractSerializer(ModelSerializer):

    class Meta:
        model  = Contract
        fields = '__all__'