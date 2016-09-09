from __future__ import unicode_literals

from django.db import models


# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(max_length=1500, verbose_name='About')
    cv_link = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
