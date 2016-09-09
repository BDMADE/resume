from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Experience(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    designation = models.CharField(max_length=250)
    department = models.CharField(max_length=250, null=True, blank=True)
    present = models.BooleanField(default=False)
    joining_date = models.DateField()
    ending_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.designation

    def __str__(self):
        return self.designation


class Todo(models.Model):
    description = models.CharField(max_length=400)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description
