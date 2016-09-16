from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Website
from about.models import About
from skill.models import Skill
from experience.models import Experience
from project.models import Project
from certificate.models import Certificate
from contact.models import Contact
from online.models import Online


# Create your views here.
def home(request):
    website = Website.objects.last()
    about = About.objects.last()
    skills = Skill.objects.all().prefetch_related('subskill_set').order_by('created_at')
    experiences = Experience.objects.all().prefetch_related('todo_set').order_by('created_at').reverse()
    projects = Project.objects.all().prefetch_related('projectlist_set').order_by('created_at').reverse()
    certificates = Certificate.objects.all().order_by('created_at').reverse()
    contact = Contact.objects.last()
    onlines = Online.objects.all()

    context = {'website': website,
               'about': about,
               'skills': skills,
               'experiences': experiences,
               'projects': projects,
               'certificates': certificates,
               'contact': contact,
               'onlines': onlines
               }
    return render(request, 'website.html', context)
