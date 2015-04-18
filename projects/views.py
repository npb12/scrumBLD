from django.shortcuts import render
from django.http import JsonResponse
from projects.models import Project, Request, EditProjectForm, ProjectSkill, Skill, AddProjectSkillForm
from users.models import Message
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django import forms

import json
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
@login_required
def edit_project(request, pid=None):

  # the newProject flag is used to direct the user when creating
  # a brand new project to the "skills" page
  newProject = True
  if pid != None:
    newProject = False
    p = Project.objects.get(pk = pid)

  if request.method == 'POST':
    if pid == None:
      form = EditProjectForm(request.POST)
    else:
      form = EditProjectForm(request.POST, instance = p)
    if form.is_valid():
      tmp = form.save(commit=False)
      tmp.createdBy = request.user
      tmp.save()

      url = "/projects/project-skills/" + str(tmp.pk) + "/"
      return HttpResponseRedirect(url)

  else:
    if pid == None:
      form = EditProjectForm()
    else:
      form = EditProjectForm(instance = p)

  c = {
        'title': 'Project Details',
        'form': form,
  }
  return render(request, "pages/projects/edit.html", c)

def temp_project_skills(request, pid):
  # Temp view until I can iron out a better way...

  p = Project.objects.get(pk = pid)
  skills = ProjectSkill.objects.filter(project = p)

  if request.method == "POST":
    form = AddProjectSkillForm(request.POST)
    if form.is_valid():
      tmp = form.save(commit = False)
      tmp.project = p
      tmp.save()

  else:
    form = AddProjectSkillForm(initial = {'project': p})

  c = {
      'title': 'Add Required Skills',
      'form': form,
      'skills': skills,
      'p': p,
      }
  return render(request, "pages/projects/temp_skills.html", c)




def project_skills(request, pid):
  project = Project.objects.get(pk = pid)
  current_skills = ProjectSkill.objects.filter(project = project)

  webSkills = Skill.objects.filter(category = "W")
  projectWebSkills = ProjectSkill.objects.filter(project = project)
  for p in projectWebSkills:
    webSkills = webSkills.exclude(pk = p.skill.pk)

  busSkills = Skill.objects.filter(category = "B")
  projectSkills = Skill.objects.filter(category = "P")
  otherSkills = Skill.objects.filter(category = "O")

  c = {
          'title': 'Skills Required - ' + project.title,
          'project': project,
          'current_skills': current_skills,
          'webSkills': webSkills,
          'busSkills': busSkills,
          'projectSkills': projectSkills,
          'otherSkills': otherSkills,
          }
  return render(request, "pages/projects/skills.html", c)
  

def projects(request):

  projects = Project.objects.all()
  c = {
      'projects': projects,
      'title': 'Projects',
  }
  return render(request, "pages/projects/projects.html", c)


def addRemoveSkill(request, pid, sid, ar):
  # pid = Project ID
  # sid = Skill ID
  # ar = Add or Remove. "A" = Add, "R" = Remove

  project = Project.objects.get(pk = pid)
  skill = Skill.objects.get(pk = sid)


  if ar == "A":
    print("in the ADD section")
    ps = ProjectSkill(project = project, skill = skill)
    ps.save()

  elif ar == "R":
    print("in the remove section")
    ps = ProjectSkill.objects.filter(project = project).filter(skill = skill)
    for p in ps:
      p.project = None
      p.skill = None
      p.delete()

  response = JsonResponse({'success':'true'})

  return HttpResponse(response)


def details(request, pid):
  project = Project.objects.get(pk = pid)
  team = Request.objects.filter(requestedProject = project).filter(isRequestAccepted = True)
  projectSkills = ProjectSkill.objects.filter(project = project)
  if request.user.is_authenticated():
    inTeam = Request.objects.filter(requestedProject = project).filter(requestedBy = request.user).filter(isRequestAccepted = True).exists()
    requested = Request.objects.filter(requestedProject = project).filter(requestedBy = request.user).filter(isRequestAccepted = False).exists()
  else:
    inTeam = False
    requested = False

  c = {
          'title': project.title,
          'project': project,
          'projectSkills': projectSkills,
          'team': team,
          'inTeam': inTeam,
          'requested': requested,
    }
  return render(request, "pages/projects/details.html", c)


@login_required
def request_to_join(request, pid):
  project = Project.objects.get(pk = pid)
  msg = request.user.username + " would like to join your team for the project: " + project.title
  newMsg = Message(fromUser = request.user, toUser = project.createdBy, message = msg)
  newMsg.save()

  newRq = Request(requestedProject = project, requestedBy = request.user)
  newRq.save()

  url = "/projects/details/" + pid + "/"
  return HttpResponseRedirect(url)

@login_required
def requests(request, pid):
  
  project = Project.objects.get(pk = pid)
  team = Request.objects.filter(requestedProject = project).filter(isRequestAccepted = True)
  projectSkills = ProjectSkill.objects.filter(project = project)
  requests = Request.objects.filter(requestedProject = project)

  c = {
          'title': 'Requests',
          'requests': requests,
          'project': project,
          'projectSkills': projectSkills,
          'team': team,
    }
  return render(request, "pages/projects/requests.html", c)

def update_request(request, rid, pid):
  r = Request.objects.get(pk = rid)
  print(r)
  if r.isRequestAccepted == True:
    print("setting to false")
    r.isRequestAccepted = False
    r.save()
  else:
    print("setting to true")
    r.isRequestAccepted = True
    r.save()

  ret = request.REQUEST.get('next', reverse("projects.views.details", args=(pid,)))
  return HttpResponseRedirect(ret)
  


