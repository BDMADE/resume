from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Website


# Create your views here.
def home(request):
    name = Website.name
    context = {'name': name}
    return render(request, 'website.html', context)
