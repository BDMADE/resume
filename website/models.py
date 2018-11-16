from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Website(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    logo = models.ImageField(max_length=255, upload_to='images/logo/')
    favicon_icon = models.ImageField(max_length=255, upload_to='images/favicon/')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
