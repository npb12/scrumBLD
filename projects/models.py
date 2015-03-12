from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

import datetime

from users.models import UserProfile




class Project(models.Model):
  title = models.CharField(verbose_name = "Title", max_length = 144)
  description = models.TextField(verbose_name = "Description")
  createdOn = models.DateField(verbose_name = "Date Created", default = datetime.datetime.today())
  createdBy = models.ForeignKey(User, verbose_name = "Creator")

  def __unicode__(self):
    return self.title

  class Meta:
    ordering = ['title']

# tracks people requesting to join a project
class Requests(models.Model):
  requestedProject = models.ForeignKey(Project, verbose_name = "Which project?")
  requestedBy = models.ForeignKey(User, verbose_name = "Which Users?")
  requestedOn = models.DateField(verbose_name = "Date requested", default = datetime.datetime.today())
  isRequestAccepted = models.BooleanField(default = False, verbose_name = "Request Accepted?")

  def __unicode__(self):
    return self.requestedBy

  