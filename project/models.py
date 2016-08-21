from __future__ import unicode_literals

from django.db import models
from icon.models import Icon


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    icon = models.OneToOneField(Icon, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Gem(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ProjectList(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255, null=True, blank=True)
    download_link = models.CharField(max_length=255, null=True, blank=True)
    bitbucket_link = models.CharField(max_length=255, null=True, blank=True)
    website_link = models.CharField(max_length=255, null=True, blank=True)
    tools = models.ManyToManyField(Tool, blank=True)
    gems = models.ManyToManyField(Gem, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
