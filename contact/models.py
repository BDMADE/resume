from __future__ import unicode_literals

from django.db import models
from icon.models import Icon


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(max_length=500)
    icon = models.OneToOneField(Icon, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    types = models.ManyToManyField(Type)
    icon = models.OneToOneField(Icon, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
