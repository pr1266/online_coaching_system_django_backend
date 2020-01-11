from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):

    username   = models.CharField(max_length = 250, primary_key = True)
    password   = models.CharField(max_length = 250)
    role       = models.CharField(max_length = 250, null = True)
    last_visit = models.DateTimeField(null = True, blank = True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):

        return self.username


class City(models.Model):

    name = models.CharField(max_length = 100, null = True)

    def __str__(self):

        return self.name

class Athlete(models.Model):
    user       = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100, null = True)
    last_name  = models.CharField(max_length = 100, null = True)
    nat_code   = models.CharField(max_length = 100, primary_key = True)
    city       = models.ForeignKey(City, on_delete = models.CASCADE)
    picture    = models.ImageField(upload_to = 'athlete/', null = True)
    
    def __str__(self):
        
        return self.first_name + ' ' + self.last_name

class Coach(models.Model):
    user       = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100, null = True)
    last_name  = models.CharField(max_length = 100, null = True)
    nat_code   = models.CharField(max_length = 100, primary_key = True)
    city       = models.ForeignKey(City, on_delete = models.CASCADE)
    degree     = models.CharField(max_length = 100, null = True)
    picture    = models.ImageField(upload_to = 'coach/', null = True)

    def __str__(self):

        return self.first_name + ' ' + self.last_name

class Records(models.Model):
    coach   = models.ForeignKey(Coach, on_delete = models.CASCADE)
    text    = models.CharField(max_length = 100, null = True)
    year    = models.IntegerField(default = 2000, null = True)

class Contract(models.Model):

    athlete = models.ForeignKey(Athlete, on_delete = models.CASCADE)
    coach   = models.ForeignKey(Coach, on_delete = models.CASCADE)
    status  = models.BooleanField(default = False)

    def __str__(self):

        return str(self.id)

