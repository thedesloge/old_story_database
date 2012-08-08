import os
import datetime
from django.db import models
from story_database.zipstorage import ZipStorage
from django.template.defaultfilters import slugify
from hvad.models import TranslatableModel, TranslatedFields

# Create your models here.
class Site(models.Model):
  domain = models.CharField(max_length=200, unique=True)
  
  def __unicode__(self):
    return self.domain

  def save(self, *args, **kwargs):
      print "saving something here"
      print self.domain
      super(Site, self).save(*args, **kwargs)
      
class Story(TranslatableModel):
    slug = models.SlugField()
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        video = models.ManyToManyField('Video', null=True, blank=True)
    )
      
class Video(models.Model):

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  title = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100)
  description = models.TextField(blank=True, null=True)
  vimeo_id = models.IntegerField()
  thumbnail = models.FileField(upload_to='uploads/video/thumbnails/%Y/%m/%d', blank=True, null=True)  
  tags = models.ManyToManyField("Tag", verbose_name="Tags",blank=True, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

  def __unicode__(self):
    return self.name

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
