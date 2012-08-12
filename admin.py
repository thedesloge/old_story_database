from django.contrib import admin
from story_database.models import *
from hvad.admin import TranslatableAdmin
from django.conf import settings
from django.contrib.sites.models import Site

class StoryAdmin(TranslatableAdmin):
    filter_horizontal = ['sites', 'tags']
    list_filter = ('sites','tags',)
    prepopulated_fields = {'slug': ('internal_id',)}
    
class TagAdmin(TranslatableAdmin):
    display_list = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
class PhotoGalleryAdmin(TranslatableAdmin):
    display_list = ('slug',)
    
class PhotoAdmin(TranslatableAdmin):
    display_list = ('slug',)
    
    
    
admin.site.register(Story, StoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(VideoStory, StoryAdmin)
admin.site.register(InfographicStory, StoryAdmin)
admin.site.register(PhotoStory, StoryAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video)
admin.site.register(InfographicPackage)
