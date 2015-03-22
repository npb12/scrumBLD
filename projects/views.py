from django.shortcuts import render
from projects.models import Project, Request, EditProjectForm
from django.contrib.auth.decorators import login_required
from django import forms

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
      form.save()

      # if it's a new project, take them to step two which will be adding
      # the required skills for the project
      if newProject:
        url = "projects/edit-skills/" + pid + "/"
        return HttpResponseRedirect(url)
      # Otherwise (not new) just go back to the project page
      return HttpResponseRedirect("projects/project/")

  else:
    if pid == None:
      form = EditProjectForm()
    else:
      form = EditProjectForm(instance = p)

  c = {
        'title': 'Project Details',
        'form': form,
  }
  return render(request, "pages/projects/project_details.html", c)

def projects(request):

  projects = Project.objects.all()
  c = {
      'projects': projects,
      'title': 'Projects',
  }
  return render(request, "pages/projects/projects.html", c)


def details(request, pid):
  project = Project.objects.get(pk = pid)
  team = Request.objects.filter(requestedProject = project).filter(isRequestAccepted = True)
  

  c = {
          'title': project.title,
          'project': project,
          'team': team,
    }
  return render(request, "pages/projects/project_home.html", c)
