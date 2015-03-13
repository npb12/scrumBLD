from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


# This extends the User model, giving us additional fields 
# to attach to the User model
class UserProfile(models.Model):
  user = models.OneToOneField(User)
  github = models.URLField(verbose_name = "GitHub Account", blank = True, null = True)

  def __unicode__(self):
    return self.user

  class Meta:
    ordering = ['user']

