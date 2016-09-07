from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Website
from about.models import About
from skill.models import Skill, Subskill


# Create your views here.
def home(request):
    website = Website.objects.last()
    about = About.objects.last()
    skills = Skill.objects.all().prefetch_related('subskill_set')

    context = {'website': website,
               'about': about,
               'skills': skills
               }
    return render(request, 'website.html', context)
