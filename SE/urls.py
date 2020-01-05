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
    path('user_role/<username>/', views.UserRole.as_view()),
    url('createuser/', views.UserCreateAPIView.as_view(), name = 'create user'),
    url(r'^user/$' , views.UserListAPIView.as_view()),
    url(r'^user/(?P<username>[\w-]+)/$' , views.UserDetailAPIView.as_view() , name = 'detail'),
    url(r'^user/(?P<username>[\w-]+)/edit/$' , views.UserUpdateAPIView.as_view() , name = 'edit'),
    url(r'^user/(?P<username>[\w-]+)/delete/$' , views.UserDeleteAPIView.as_view() , name = 'delete'),
]
