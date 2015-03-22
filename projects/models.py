from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

import datetime

from users.models import UserProfile




class Skills(models.Model):
  needsJavaDev = models.BooleanField(default= False, verbose_name = "Java")
  needsFrontEndDev = models.BooleanField(default = False, verbose_name = "Frontend Dev")
  needsMarketing = models.BooleanField(default = False, verbose_name = "Marketing")



class Project(models.Model):
  title = models.CharField(verbose_name = "Project Name", max_length = 144)
  description = models.CharField(verbose_name = "Project Description", max_length = 500)
  details = models.TextField(verbose_name = "Project Details")
  createdOn = models.DateField(verbose_name = "Date Created", default = datetime.datetime.today())
  createdBy = models.ForeignKey(User, verbose_name = "Creator")
  skills = models.ForeignKey(Skills, verbose_name = "Required Skills", blank = True, null = True)
  isPrivate = models.BooleanField(default = False, verbose_name = "Private")

  def __unicode__(self):
    return self.title

  class Meta:
    ordering = ['title']


# tracks people requesting to join a project
class Request(models.Model):
  requestedProject = models.ForeignKey(Project, verbose_name = "Which project?")
  requestedBy = models.ForeignKey(User, verbose_name = "Which Users?")
  requestedOn = models.DateField(verbose_name = "Date requested", default = datetime.datetime.today())
  isRequestAccepted = models.BooleanField(default = False, verbose_name = "Request Accepted?")

  def __unicode__(self):
    return self.requestedBy.username

  
class EditProjectForm(ModelForm):
    class Meta:
      model = Project
      fields = ('title', 'description', 'details', 'isPrivate',)


