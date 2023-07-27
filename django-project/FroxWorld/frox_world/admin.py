from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Privilege)
admin.site.register(PrivilegeType)
admin.site.register(Purchase)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Server)