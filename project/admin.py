from django.contrib import admin
from .models import Project, Tool, Gem, ProjectList

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectList)
admin.site.register(Tool)
admin.site.register(Gem)
