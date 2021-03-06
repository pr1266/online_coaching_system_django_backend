from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from test1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
    
    #! users urls:
    url('createuser/', views.UserCreateAPIView.as_view(), name = 'create user'),
    url(r'^user/$' , views.UserListAPIView.as_view()),
    url(r'^user/(?P<username>[\w-]+)/$' , views.UserDetailAPIView.as_view() , name = 'detail'),
    url(r'^user/(?P<username>[\w-]+)/edit/$' , views.UserUpdateAPIView.as_view() , name = 'edit'),
    url(r'^user/(?P<username>[\w-]+)/delete/$' , views.UserDeleteAPIView.as_view() , name = 'delete'),

    #TODO city urls:
    url(r'^city/$' , views.CityListAPIView.as_view()),
    url(r'^city/(?P<id>[\w-]+)/$' , views.CityDetailAPIView.as_view() , name = 'detail'),
    url(r'^city/(?P<id>[\w-]+)/edit/$' , views.CityUpdateAPIView.as_view() , name = 'edit'),
    url(r'^city/(?P<id>[\w-]+)/delete/$' , views.CityDeleteAPIView.as_view() , name = 'delete'),

    #? coaches urls:
    url(r'^coach/$' , views.CoachListAPIView.as_view()),
    url(r'^coach/(?P<user__username>[\w-]+)/$' , views.CoachDetailAPIView.as_view() , name = 'detail'),
    url(r'^coach/(?P<user__username>[\w-]+)/edit/$' , views.CoachUpdateAPIView.as_view() , name = 'edit'),
    url(r'^coach/(?P<user__username>[\w-]+)/delete/$' , views.CoachDeleteAPIView.as_view() , name = 'delete'),
    url('createcoach/', views.CoachCreateAPIView.as_view()),
    #!!!
    url(r'^coach_/(?P<nat_code>[\w-]+)/$' , views.CoachDetailAPIView_.as_view() , name = 'detail'),

    #* athlets urls:
    url(r'^athlete/$' , views.AthleteListAPIView.as_view()),
    url(r'^athlete/(?P<nat_code>[\w-]+)/$' , views.AthleteDetailAPIView.as_view() , name = 'detail'),
    url(r'^athlete/(?P<nat_code>[\w-]+)/edit/$' , views.AthleteUpdateAPIView.as_view() , name = 'edit'),
    url(r'^athlete/(?P<nat_code>[\w-]+)/delete/$' , views.AthleteDeleteAPIView.as_view() , name = 'delete'),
    url('createathlete/', views.AthleteCreateAPIView.as_view()),
    #! contracts urls
    url('createcontract/', views.ContractCreateAPIView.as_view(), name = 'create contract'),
    url(r'^contract/$' , views.ContractListAPIView.as_view()),
    url(r'^contract/(?P<id>[\w-]+)/$' , views.ContractDetailAPIView.as_view() , name = 'detail'),
    url(r'^contract/(?P<id>[\w-]+)/edit/$' , views.ContractUpdateAPIView.as_view() , name = 'edit'),
    url(r'^contract/(?P<id>[\w-]+)/delete/$' , views.ContractDeleteAPIView.as_view() , name = 'delete'),
    
    url(r'^coachofathlete/$', views.CoachesOfAthletes.as_view()),
    url(r'athletsofcoach/$', views.AthletesOfCoach.as_view()),
    url(r'requestsofcoach/$', views.RequestsOfCoach.as_view()),

    path('get_username_athlete/', views.get_username_athlete),
    path('get_username_coach/', views.get_username_coach),
    path('search_city/',views.search_city),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)