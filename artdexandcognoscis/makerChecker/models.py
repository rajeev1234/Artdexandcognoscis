from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from django.conf import settings


class User(AbstractUser):
    is_maker = models.BooleanField(default=False)
    is_checker = models.BooleanField(default=False)


class Make(models.Model):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_make")
    dateDiscountine = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
    is_authorise = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_model")
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='model')
    dateDiscountine = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
    is_authorise = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Variant(models.Model):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_variant")
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='variant')
    cc = models.FloatField(null=True,blank=True)
    dateDiscountine = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
    is_authorise = models.BooleanField(default=False)


    def __str__(self):
        return self.name





