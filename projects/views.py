from django.shortcuts import render
from projects.models import Project, create_project
from django.contrib.auth.decorators import login_required
from django import forms

from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
@login_required
def create(request):
  if request.method == 'POST':
    print("creating")
    form = create_project(request.POST)
    if form.is_valid():
      print("is valid")
      tmp = form.save(commit=False)
      tmp.createdBy = request.user
      form.save()
      return HttpResponseRedirect("projects/project/")
  else:
      form = create_project()
  c = {
      'form': form,
          }
  return render(request, "pages/projects/create.html", c)

"""
def projects(request):

  c = {
      'projects': Projec,
  }
  return render(request, "pages/projects/projects.html", c)

def open_project(request):
  if request.method == 'GET':
    if request.GET.has_key('pid'):
      pid = request.GET['pid']
      p = Project.objects.get(pk = pid)
      c = {
        'project': p,
            }
      return render(request, "pages/projects/project_home.html", c)
"""
