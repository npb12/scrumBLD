from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

import datetime


# This extends the User model, giving us additional fields 
# to attach to the User model
class UserProfile(models.Model):
  user = models.OneToOneField(User)
  lastConvo = models.CharField(max_length = 5, verbose_name = "PK of last conversation", blank = True, null = True)
  github = models.URLField(verbose_name = "GitHub Account", blank = True, null = True)

  def __unicode__(self):
    return self.user.username

  class Meta:
    ordering = ['user']

class Associate(models.Model):
  requesting = models.ForeignKey(User, verbose_name = "Who is making the request?", related_name = "requesting_user")
  requested = models.ForeignKey(User, verbose_name = "Which user would they like to connect with?", related_name = "requested_user")
  dateRequested = models.DateField(default = datetime.date.today(), verbose_name = "Date Requested")
  dateAccepted = models.DateField(verbose_name = "Date Accepted", blank = True, null = True)
  dateRemoved = models.DateField(verbose_name = "Date Removed", blank = True, null = True)

  def __unicode__(self):
    return u'%s -- requested --> %s' % (self.requesting.username, self.requested.username)



class Message(models.Model):
  fromUser = models.ForeignKey(User, verbose_name = "From", related_name = 'from_user')
  toUser = models.ForeignKey(User, verbose_name = "To", related_name = 'to_user')
  message = models.TextField(verbose_name = "Message")
  dateSent = models.DateTimeField(default = datetime.datetime.now(), verbose_name = "Date Sent")
  isSeen = models.BooleanField(default = False, verbose_name = "Seen?")

  def __unicode__(self):
    return u'%s - %s' % (self.fromUser.username, self.dateSent)


class NewMessageForm(ModelForm):
  class Meta:
    model = Message
    fields = ('message', 'toUser', 'fromUser')

class EditProfileForm(ModelForm):
  class Meta:
    model = UserProfile
    fields = ('github',)
