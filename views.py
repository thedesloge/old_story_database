from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import *
from story_database.models import *
from django.conf import settings
from django.contrib.sites.models import Site
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

def index(request, language_code='en', story_slug=""):
    meta = request.META
    site = request.get_host()
    current_site = Site.objects.get_current()
    
    stories = Story.objects.filter(sites__in=[current_site])
    
    return HttpResponse(str(stories.all()) + " blah blah")

def site_status(request):
    try:
        return direct_to_template(request, template="site_status.html")
    except TemplateDoesNotExist:
        raise Http404