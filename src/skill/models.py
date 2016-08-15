from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class Subskill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


def __unicode__(self):
    return self.name
    return self.link


def __str__(self):
    return self.name
    return self.link