from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Experience(models.Model):
    designation = models.CharField(max_length=250)
    department = models.CharField(max_length=250, null=True)
    present = models.BooleanField(default=False)
    joining_date = models.DateField()
    ending_date = models.DateField(null=True)

    def __unicode__(self):
        return self.designation

    def __str__(self):
        return self.designation