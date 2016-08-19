from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Website(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(max_length=255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
