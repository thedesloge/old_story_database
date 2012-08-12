import os
import datetime
from django.db import models
from story_database.zipstorage import ZipStorage
from django.template.defaultfilters import slugify
from hvad.models import TranslatableModel, TranslatedFields
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# Create your models here.
      
class Story(TranslatableModel):
    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"
    
    internal_id = models.CharField(max_length=100)
    slug = models.SlugField()
    sites = models.ManyToManyField(Site)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        headline = models.CharField(max_length=100),
        description = models.TextField()
    )
    
    def __unicode__(self):
        return self.slug
    
class VideoStory(TranslatableModel):
    class Meta:
        verbose_name = "Video Story"
        verbose_name_plural = "Video Stories"
    
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    internal_id = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    sites = models.ManyToManyField(Site)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        headline = models.CharField(max_length=255),
        description = models.TextField(),
        vimeo_id = models.IntegerField()
    )
    
    def __unicode__(self):
        return self.slug
    
class InfographicStory(TranslatableModel):
    class Meta:
        verbose_name = "Infographic Story"
        verbose_name_plural = "Infographic Stories"
     
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)   
    internal_id = models.CharField(max_length=100, unique=True)  
    slug = models.SlugField()
    sites = models.ManyToManyField(Site)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    infographic_package = models.ForeignKey('InfographicPackage', blank=True, null=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        headline = models.CharField(max_length=255),
        description = models.TextField(),
    )
    
    def __unicode__(self):
        return self.internal_id

class PhotoStory(TranslatableModel):
    class Meta:
        verbose_name = "Photo Story"
        verbose_name_plural = "Photo Stories"
     
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)   
    internal_id = models.CharField(max_length=100, unique=True)  
    slug = models.SlugField()
    sites = models.ManyToManyField(Site)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    photo_gallery = models.ForeignKey('PhotoGallery', null=True, blank=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        headline = models.CharField(max_length=255),
        description = models.TextField()
    )
    
    def __unicode__(self):
        return self.internal_id
    
class Video(TranslatableModel):
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
    
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=100)
    thumbnail = models.FileField(upload_to='uploads/video/thumbnails/%Y/%m/%d', blank=True, null=True)  
    tags = models.ManyToManyField("Tag", verbose_name="Tags",blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        headline = models.CharField(max_length=255),
        description = models.TextField(),
        vimeo_id = models.IntegerField()
    )

    def __unicode__(self):
        return self.title

class InfographicPackage(TranslatableModel):
    class Meta:
        verbose_name = "Infographic Package"
        verbose_name_plural = "Infographic Packages"
        
    slug = models.SlugField()
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        headline = models.CharField(max_length=255),
        description = models.TextField(),
        infographic_bundle = models.FileField(upload_to="uploads/infographics")
    )
    
class PhotoGallery(TranslatableModel):
    class Meta:
        verbose_name = "Photo Gallery"
        verbose_name_plural = "Photo Galleries"
        
    slug = models.SlugField()
    photos = models.ManyToManyField('Photo', blank=True, null=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        headline = models.CharField(max_length=255),
        description = models.TextField(),
    )
    
class Photo(TranslatableModel):
    
    slug = models.SlugField()
    file = models.FileField(upload_to='uploads/currentSite/photos/%Y/%m/%d')
    
    translations = TranslatedFields(
        caption = models.TextField(),
    )
    

class Video_Background(models.Model):
    class Meta:
        verbose_name = "Background Video"
        verbose_name_plural = "Background Videos"

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    h264_background = models.FileField(upload_to="uploads/background-video/h264")
    ogg_background = models.FileField(upload_to="uploads/background-video/ogg")
    jpg_background = models.FileField(upload_to="uploads/background-video/jpg")

    def __unicode__(self):
        return self.name

#Start Tag model
class Tag(TranslatableModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    
    translations = TranslatedFields(
        tag_translation = models.CharField(max_length=25),
    )
    
    def __unicode__(self):
        return "Tag: " + self.name