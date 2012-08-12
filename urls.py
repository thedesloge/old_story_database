from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from story_database.handlers import *
from story_database.models import *
from django.views.generic import list_detail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.contrib.sites.models import Site

story_handler = Resource(StoryHandler)
video_handler = Resource(VideoHandler)
urlpatterns = patterns('',
 
    url(r'^api/story/$', story_handler),
    url(r'^api/story/(?P<story_id>\d)/$', story_handler),
    
    url(r'^api/video/$', video_handler),
    url(r'^api/video/(?P<video_id>\d)/$', video_handler)

)

story = {
    'queryset' : Story.objects.filter(sites__in=[Site.objects.get_current()]),
    'template_name' : 'story_list.html',
    'extra_context' : {'video_story_list': VideoStory.objects.filter(sites__in=[Site.objects.get_current()]),
                       'photo_story_list': PhotoStory.objects.filter(sites__in=[Site.objects.get_current()]),
                       'infographic_story_list': InfographicStory.objects.filter(sites__in=[Site.objects.get_current()]),
                       'site_name': Site.objects.get_current()}
}
urlpatterns += patterns('story_database.views',
     url(r'^$', 'index'),
     url(r'^story/(?P<story_slug>.*)/$', 'index'),     
     url(r'^story/(?P<language_code>en|es)/(?P<story_slug>.*)/$', 'index'),
     
     url(r'^story_list/$', login_required(list_detail.object_list), story),
     
     url(r'^accounts/login/$', login),
     
)

