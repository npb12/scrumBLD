from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

import datetime


# This extends the User model, giving us additional fields 
# to attach to the User model
class UserProfile(models.Model):
  user = models.OneToOneField(User)
  github = models.URLField(verbose_name = "GitHub Account", blank = True, null = True)

  def __unicode__(self):
    return self.user

  class Meta:
    ordering = ['user']

class Friend(models.Model):
  requesting = models.ForeignKey(User, verbose_name = "Requesting User", related_name = "requesting_user")
  requested = models.ForeignKey(User, verbose_name = "Requested User", related_name = "requested_user")
  dateRequested = models.DateField(default = datetime.date.today(), verbose_name = "Date Requested")
  dateAccepted = models.DateField(default = datetime.date.today(), verbose_name = "Date Accepted")

  def __unicode__(self):
    return self.requested

