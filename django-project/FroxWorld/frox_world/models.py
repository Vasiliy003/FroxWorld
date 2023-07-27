from django.db import models

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
    image = models.ImageField()
    skin = models.ImageField()

class User(models.Model):
    login = models.CharField(max_length=150, null=False, blank=False, default="Georgiy")
    password = models.CharField(max_length=150, null=False, blank=False, default=123)
    email = models.EmailField()
    profile = models.OneToOneField(
        'Profile', on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.login
    
class Server(models.Model):
    ip = models.IntegerField(null=False)
    name = models.CharField(max_length=150, null=False, blank=False, default="qwerty-serv")

    def __str__(self):
        return self.name
    