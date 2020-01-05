from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , UpdateAPIView , DestroyAPIView
from .models import *
from .serializer import *
from django.core import serializers
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes , api_view
from django.db.models import F
from django.http import JsonResponse , HttpResponse
from rest_framework.permissions import(
    AllowAny ,
    IsAuthenticated ,
    IsAdminUser ,
    IsAuthenticatedOrReadOnly ,
)
from django.views.generic import View
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST
from rest_framework.filters import(
    SearchFilter ,
    OrderingFilter ,
)
from django.db.models import Count, Case, When, IntegerField
import datetime
import time
import json


class ContractListAPIView(ListAPIView):

    queryset           = Contract.objects.all()
    serializer_class   = ContractSerializer
    permission_classes = [IsAuthenticated,]
    search_fields = ['__all__']

class ContractDetailAPIView(RetrieveAPIView):

    queryset           = Contract.objects.all()
    serializer_class   = ContractSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class ContractUpdateAPIView(UpdateAPIView):

    queryset = Contract.objects.all()
    serializer_class =  ContractSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]

class ContractDeleteAPIView(DestroyAPIView):

    queryset = Contract.objects.all()
    serializer_class =  ContractSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]