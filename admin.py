from django.contrib import admin
from story_database.models import *
from hvad.admin import TranslatableAdmin

class StoryTest(TranslatableAdmin):
    all_translations = ('title')
    
admin.site.register(Story, StoryTest)
admin.site.register(Site)