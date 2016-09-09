from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=400, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=400)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
