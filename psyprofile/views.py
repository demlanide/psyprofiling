from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def index(request):
    template = loader.get_template('psyprofile/index.html')
    return HttpResponse(template.render(request))