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


class CoachesOfAthletes(ListAPIView):

    queryset           = Contract.objects.all()
    serializer_class   = ContractSerializer
    permission_classes = [IsAuthenticated,]
    search_fields      = 'id'

    def get_queryset(self , *args , **kwargs):
        
        queryset_list = Contract.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(Q(athlete__nat_code = query) & Q(status = True))

        return queryset_list

class AthletesOfCoach(ListAPIView):

    queryset           = Contract.objects.all()
    serializer_class   = ContractSerializer
    permission_classes = [IsAuthenticated,]
    search_fields      = 'id'

    def get_queryset(self , *args , **kwargs):
        
        queryset_list = Contract.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(Q(coach__nat_code = query) & Q(status = True))

        return queryset_list

class RequestsOfCoach(ListAPIView):

    queryset           = Contract.objects.all()
    serializer_class   = ContractSerializer
    permission_classes = [IsAuthenticated,]
    search_fields      = 'id'

    def get_queryset(self , *args , **kwargs):
        
        queryset_list = Contract.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(Q(coach__nat_code = query) & Q(status = False))

        return queryset_list


class ContractCreateAPIView(CreateAPIView):

    queryset = Contract.objects.all()
    serializer_class = ContractCreateSerializer
    permission_classes = [IsAuthenticated]

class ContractListAPIView(ListAPIView):

    queryset           = Contract.objects.all()
    serializer_class   = ContractSerializer
    permission_classes = [IsAuthenticated,]
    search_fields      = ['__all__']

class ContractDetailAPIView(RetrieveAPIView):

    queryset           = Contract.objects.all()
    serializer_class   = ContractSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field       = 'id'
    lookup_url_kwarg   = 'id'

class ContractUpdateAPIView(UpdateAPIView):

    queryset           = Contract.objects.all()
    serializer_class   =  ContractSerializer
    lookup_field       = 'id'
    lookup_url_kwarg   = 'id'
    permission_classes = [IsAuthenticated,]

class ContractDeleteAPIView(DestroyAPIView):

    queryset = Contract.objects.all()
    serializer_class =  ContractSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]

class UserListAPIView(ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['id', 'username']


class UserDetailAPIView(RetrieveAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'username'
    lookup_url_kwarg = 'username'

class UserDeleteAPIView(DestroyAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = 'username'
    lookup_url_kwarg = 'username'

class UserCreateAPIView(CreateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class UserUpdateAPIView(UpdateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['username', ]
    lookup_url_kwarg = 'username'

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class AthleteCreateAPIView(CreateAPIView):

    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [IsAuthenticated]

class AthleteListAPIView(ListAPIView):

    queryset           = Athlete.objects.all()
    serializer_class   = AthleteSerializer
    permission_classes = [IsAuthenticated,]
    search_fields      = ['__all__']

class AthleteDetailAPIView(RetrieveAPIView):

    queryset           = Athlete.objects.all()
    serializer_class   = AthleteSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field       = 'id'
    lookup_url_kwarg   = 'id'

class AthleteUpdateAPIView(UpdateAPIView):

    queryset           = Athlete.objects.all()
    serializer_class   =  AthleteSerializer
    lookup_field       = 'id'
    lookup_url_kwarg   = 'id'
    permission_classes = [IsAuthenticated,]

class AthleteDeleteAPIView(DestroyAPIView):

    queryset = Athlete.objects.all()
    serializer_class =  AthleteSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]

class CoachCreateAPIView(CreateAPIView):

    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [IsAuthenticated]

class CoachListAPIView(ListAPIView):

    queryset           = Coach.objects.all()
    serializer_class   = CoachSerializer
    permission_classes = [IsAuthenticated,]
    search_fields      = ['__all__']

class CoachDetailAPIView(RetrieveAPIView):

    queryset           = Coach.objects.all()
    serializer_class   = CoachSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field       = 'user__username'
    lookup_url_kwarg   = 'user__username'

class CoachDetailAPIView_(RetrieveAPIView):

    queryset           = Coach.objects.all()
    serializer_class   = CoachSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field       = 'nat_code'
    lookup_url_kwarg   = 'nat_code'

class CoachUpdateAPIView(UpdateAPIView):

    queryset           = Coach.objects.all()
    serializer_class   =  CoachSerializer
    lookup_field       = 'id'
    lookup_url_kwarg   = 'id'
    permission_classes = [IsAuthenticated,]

class CoachDeleteAPIView(DestroyAPIView):

    queryset = Coach.objects.all()
    serializer_class =  CoachSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]

class CityCreateAPIView(CreateAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

class CityListAPIView(ListAPIView):

    queryset           = City.objects.all()
    serializer_class   = CitySerializer
    permission_classes = [IsAuthenticated,]
    search_fields      = ['__all__']

class CityDetailAPIView(RetrieveAPIView):

    queryset           = City.objects.all()
    serializer_class   = CitySerializer
    permission_classes = [IsAuthenticated,]
    lookup_field       = 'id'
    lookup_url_kwarg   = 'id'

class CityUpdateAPIView(UpdateAPIView):

    queryset           = City.objects.all()
    serializer_class   =  CitySerializer
    lookup_field       = 'id'
    lookup_url_kwarg   = 'id'
    permission_classes = [IsAuthenticated,]

class CityDeleteAPIView(DestroyAPIView):

    queryset = City.objects.all()
    serializer_class =  CitySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_username_athlete(request):

    username = request.data['username']

    obj = Athlete.objects.get(user = username)
    ser_obj = AthleteSerializer(obj, many = False)

    return Response(ser_obj.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def get_username_coach(request):

    username = request.data['username']

    obj = Coach.objects.get(user = username)
    ser_obj = CoachSerializer(obj, many = False)

    return Response(ser_obj.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def search_city(request):

    city = request.data['city']
    print(city)
    city = int(city)
    obj = Coach.objects.filter(city = city)
    ser_obj = CoachSerializer(obj, many = True)

    return Response(ser_obj.data)