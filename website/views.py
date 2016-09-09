from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Website
from about.models import About
from skill.models import Skill
from experience.models import Experience
from project.models import Project
from certificate.models import Certificate


# Create your views here.
def home(request):
    website = Website.objects.last()
    about = About.objects.last()
    skills = Skill.objects.all().prefetch_related('subskill_set')
    experiences = Experience.objects.all().prefetch_related('todo_set')
    projects = Project.objects.all().prefetch_related('projectlist_set')
    certificates = Certificate.objects.all().order_by('name').reverse()
    context = {'website': website,
               'about': about,
               'skills': skills,
               'experiences': experiences,
               'projects': projects,
               'certificates': certificates
               }
    return render(request, 'website.html', context)
