from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import *
from story_database.models import *
from pprint import PrettyPrinter
from django import forms
import re

def index(request, language_code='en', story_slug=""):
    site = request.get_host()
    
    #page = Page.objects.get()
    return HttpResponse(site)