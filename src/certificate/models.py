from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=400, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=400)
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
