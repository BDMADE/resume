from __future__ import unicode_literals

from django.db import models
from icon.models import Icon


# Create your models here.

class Online(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=500)
    icon = models.OneToOneField(Icon, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
