from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

import datetime

from users.models import UserProfile




class Skill(models.Model):
  CATEGORY_CHOICES = (
          ('PW', 'Programming & IT - Web'),
          ('PM', 'Programming & IT - Mobile'),
          ('PI', 'Programming & IT - Other'),
          ('B', 'Business'),
          ('D', 'Design'),
          ('O', 'Other'),
          )

  category = models.CharField(max_length = 2, verbose_name = "Category", default = "O", choices = CATEGORY_CHOICES)
  abbreviation = models.CharField(max_length = 20, verbose_name = "Abbreviated Name for Tags", default = "??")
  fullName = models.CharField(max_length = 100, verbose_name = "Full skill name", default = "Name")
  description = models.TextField(verbose_name = "Description of Skill", blank = True, null = True)

  def __unicode__(self):
    return self.fullName



class Project(models.Model):
  title = models.CharField(verbose_name = "Project Name", max_length = 144)
  description = models.CharField(verbose_name = "Project Description", max_length = 500)
  details = models.TextField(verbose_name = "Project Details")
  createdOn = models.DateField(verbose_name = "Date Created", default = datetime.datetime.today())
  createdBy = models.ForeignKey(User, verbose_name = "Creator")
  isPrivate = models.BooleanField(default = False, verbose_name = "Private")

  def __unicode__(self):
    return self.title

  class Meta:
    ordering = ['title']


class ProjectSkill(models.Model):
  project = models.ForeignKey(Project, verbose_name = "Connected Project", null = True)
  skill = models.ForeignKey(Skill, verbose_name = "Required Skill", null = True)
  isNeeded = models.BooleanField(default = False, verbose_name = "Skill is still needed")

  def __unicode__(self):
    return u'%s - %s' % (self.skill.fullName, self.project.title)

# tracks people requesting to join a project
class Request(models.Model):
  requestedProject = models.ForeignKey(Project, verbose_name = "Which project?")
  requestedBy = models.ForeignKey(User, verbose_name = "Which Users?")
  requestedOn = models.DateField(verbose_name = "Date requested", default = datetime.datetime.today())
  isRequestAccepted = models.BooleanField(default = False, verbose_name = "Request Accepted?")

  def __unicode__(self):
    return self.requestedBy.username


class TeamMember(models.Model):
  project = models.ForeignKey(Project, verbose_name = "Connected Project")
  member = models.ForeignKey(User, verbose_name = "Team Member")
  dateJoined = models.DateField(default = datetime.datetime.today(), verbose_name = "Date Joined the Team")
  dateLeft = models.DateField(default = datetime.datetime.today(), verbose_name = "Date Left the Team")

  def __unicode__(self):
    return u'%s - %s' % (self.member.username, self.project.title)

  class Meta:
    ordering = ['member']


class TeamMemberSkill(models.Model):
  project = models.ForeignKey(Project, verbose_name = "Project")
  member = models.ForeignKey(TeamMember, verbose_name = "Team Member")
  skill = models.ForeignKey(Skill, verbose_name = "Skill")

  def __unicode__(self):
    return u'%s - %s - %s' % (self.project.title, self.member.username, self.skill.fullName)

  class Meta:
    ordering = ['project']


###### FORMS ####
  
class EditProjectForm(ModelForm):
  class Meta:
    model = Project
    fields = ('title', 'description', 'details', 'isPrivate',)

class AddProjectSkillForm(ModelForm):
  class Meta:
    model = ProjectSkill
    fields = ('skill', 'project')


    

