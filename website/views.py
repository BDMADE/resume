from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def home(request):
    return render(request, 'website.html', {})
