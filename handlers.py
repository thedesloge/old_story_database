from piston.handler import BaseHandler
from story_database.models import *

class StoryHandler(BaseHandler):
    allowed_methods = ("GET",)
    model = Story
    
    def read(self, request, story_id=None):
        
        base = Story.objects
        
        if story_id:
            return "story id: " + str(story_id) #base.get(pk=story_id)
        else:
            return "story id: " + str(story_id)
            #return base.all()
            
            
class VideoHandler(BaseHandler):
    allowed_methods = ("GET",)
    model = Video
    
    def read(self, request, video_id=None):
        
        return "video id: " + str(video_id)
