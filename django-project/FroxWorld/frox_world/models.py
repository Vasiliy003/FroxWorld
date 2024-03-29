from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PrivilegeType(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, default="Georgia")

    def __str__(self):
        return self.name

class Privilege(models.Model):
    price = models.IntegerField(null=False, default=0)
    name = models.CharField(max_length=150, null=False, blank=False, default="Privilege")
    description = models.TextField(null=False, blank=True)
    expiration = models.DateTimeField()
    privilege_type = models.ForeignKey(
        'PrivilegeType', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    cost = models.IntegerField(null=False, default=0)
    date = models.DateTimeField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, upload_to='images/')
    skin = models.ImageField(blank=True, upload_to='skins/')

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return "User-error"
    

# class User(models.Model):
#     login = models.CharField(max_length=150, null=False, blank=False, default="Georgiy")
#     password = models.CharField(max_length=150, null=False, blank=False, default=123)
#     email = models.EmailField()
#     profile = models.OneToOneField(
#         'Profile', on_delete=models.CASCADE
#     )
    
#     def __str__(self):
#         return self.login
    
class Server(models.Model):
    ip = models.IntegerField(null=False)
    name = models.CharField(max_length=150, null=False, blank=False, default="qwerty-serv")
    online = models.IntegerField(blank=False, default=0)
    max_online = models.IntegerField(blank=False, null=False, default=250)
    is_online = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    