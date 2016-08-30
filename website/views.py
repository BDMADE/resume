from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Website
from about.models import About


# Create your views here.
def home(request):
    website = Website.objects.last()
    about = About.objects.last()
    context = {'website': website,
               'about': about}
    return render(request, 'website.html', context)
