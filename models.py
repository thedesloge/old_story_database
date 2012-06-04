import os
import zipfile
import datetime
from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation
from story_database.zipstorage import ZipStorage
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify


# Create your models here.
class Site(models.Model):
  domain = models.CharField(max_length=200, unique=True)
  
  def __unicode__(self):
    return self.domain

class Page(models.Model):
    class Meta:
        verbose_name = "Pages"
        verbose_name_plural = "Pages"
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    video_background = models.ForeignKey('Video_Background')
    
    
        
class Page_Translation(MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')
  
    parent = models.ForeignKey('Page', related_name='translations')
    headline = models.CharField(max_length=100)
    single_line_description = models.CharField(max_length=200)
    description = models.TextField()
    video = models.ForeignKey('Video', related_name='Featured Video', blank=True, null=True)
    
    
    

"""class Resources(models.Model):
  class Meta:
    verbose_name = "Resource"
    verbose_name_plural = "Resources"

  name = models.CharField(max_length=100)
  slug = models.SlugField()
  resource_image = models.FileField(upload_to="uploads/resource-images")  
  url = models.URLField(blank=True, null=True)

  def __unicode__(self):
    return self.name

#Start category model
class Category(models.Model):
  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  name = models.CharField(max_length=200)
  slug = models.SlugField()

  def __unicode__(self):
    return "Category: " + self.name

class Category_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')

  parent = models.ForeignKey('Category', related_name='translations')
  translation = models.CharField(max_length=100)"""

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
class Tag(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField()
  
  def __unicode__(self):
    return "Tag: " + self.name

class Tag_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')
  
  parent = models.ForeignKey('Tag', related_name='translations')
  translation = models.CharField(max_length=100)


class Video(models.Model):

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  title = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100)
  description = models.TextField(blank=True, null=True)
  vimeo_id = models.IntegerField()
  thumbnail = models.FileField(upload_to='uploads/video/thumbnails/%Y/%m/%d', blank=True, null=True)  
  tags = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

  def __unicode__(self):
    return self.name

#Related Content Fields
"""class Related_Content(models.Model):
  class Meta:
    verbose_name = "Related Content"
    verbose_name_plural = "Related Content"

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)
  tag = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)

  def __unicode__(self):
    return self.name

class Related_Content_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')

  parent = models.ForeignKey('Related_Content', related_name='translations')
  videos = models.ManyToManyField(Video, verbose_name="Videos",blank=True, null=True)
  infographics = models.ManyToManyField(Infographic, verbose_name="Infographics",blank=True, null=True)
  photo_galleries = models.ManyToManyField(Photo_Gallery, verbose_name="Photo Galleries",blank=True, null=True) 
  
#End Related Content

class Story(models.Model):
  class Meta:
    verbose_name_plural = "Story"

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  title = models.CharField(max_length=200)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)
  tags = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

  def __unicode__(self):
    return self.name 

class Story_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')
  
  parent = models.ForeignKey('Story', related_name='translations')

  headline = models.CharField(max_length=300 )
  subheadline = models.CharField(max_length=300)
  single_line_description = models.CharField(max_length=300)
  description = models.TextField()
  quote = models.TextField(blank=True, null=True)
  quote_attribution = models.TextField(blank=True, null=True)
  poster_frame = models.ForeignKey(Poster_Frame, blank=True, null=True)
  featured_video = models.ForeignKey(Video, blank=True, null=True)
  related_content = models.ForeignKey(Related_Content, blank=True, null=True) 
  
  def __unicode__(self):
    return "Story Translation"

class Research(models.Model):
  class Meta:
    verbose_name_plural = "Research"
    
  name = models.CharField(max_length=30)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)

  def __unicode__(self):
    return self.name
  
class Research_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')

  parent = models.ForeignKey('Research', related_name='translations')
  title = models.CharField(max_length=100)
  institute = models.CharField(max_length=100)
  short_description = models.TextField()
  url = models.URLField(blank=True, null=True)"""

