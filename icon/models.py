from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Icon(models.Model):
    name = models.CharField(max_length=256)
    icon_attribute = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
