from __future__ import unicode_literals

from django.db import models


# Create your models here.
class About(models.Model):
    class Meta:
        verbose_name = 'About'
        verbose_plural_name = 'Abouts'

    details = models.TextField(max_length=1500, verbose_name='About')
    download = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
