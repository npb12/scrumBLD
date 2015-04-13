from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Min, Q
from itertools import chain
from django.core import serializers

from django.contrib.auth.models import User
from users.models import UserProfile, Associate, Message, NewMessageForm
from projects.models import Project

import datetime


def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      profile = UserProfile(user = new_user)
      profile.save()
      if len(request.POST['password1']) > 5:
        new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        login(request, new_user)
        return HttpResponseRedirect("/landing/")
  else:
    form = UserCreationForm()
  return render(request, "registration/register.html", { 'form': form, })

@login_required
def dashboard(request):
  
  associates = Associate.objects.filter(Q(requesting = request.user) | Q(requested = request.user)).exclude(dateAccepted = None).filter(dateRemoved = None)
  projects = Project.objects.filter(createdBy = request.user)
  c = {
          'title': "Dashboard",
          'associates': associates,
          'projects': projects,
          }
  return render(request, "pages/users/dashboard.html", c)


@login_required
def new_message(request):
  
  to = ""
  if request.method == 'POST':
    form = NewMessageForm(request.POST)
    if form.is_valid():
      tmp = form.save(commit = False)
      tmp.save()
      return HttpResponseRedirect("/user/messages/" + str(tmp.toUser.pk) + "/")
  else:
    toID = request.GET['to']
    to = User.objects.get(pk=toID)
    frm = User.objects.get(pk=request.user.pk)
    cancel = request.path

    form = NewMessageForm(initial={'fromUser':frm,'toUser':to})
  c = {
      'to': str(to),
      'title': "New Message to " + str(to),
      'form': form,
      'cancel': cancel,
      }
  return render(request, "pages/users/new_message.html", c)


# Gets all messages between just two people
@login_required
def get_messages(request):

  if request.method == "GET":
    to = request.GET['to']
    frm = request.GET['from']
    msgs = Message.objects.filter(Q(toUser = to) | Q(toUser = frm)).filter(Q(fromUser = to) | Q(fromUser = frm)).order_by('dateSent')

    usr = User.objects.get(pk=to)
    usr.userprofile.lastConvo = frm
    usr.userprofile.save()

    for m in msgs:
      # Once loaded, all messages will have been "seen"
      m.isSeen = True
      m.save()

  json = serializers.serialize('json', msgs)

  return HttpResponse(json)
  


@login_required
def messages(request, convoPK=None):
  
  to = request.user.pk
  msgs = Message.objects.filter(Q(toUser = to) | Q(fromUser = to)).order_by('dateSent')

  # This query just gets a unique list of user.pks who have conversations with the main user
  # this list is used to create the list of conversations on the left side of the page
  convos = Message.objects.filter(toUser = request.user.pk).values('fromUser').distinct()
  
  # Create a new array to hold all the User objects that
  # have messaged the main User
  convo_list = []
  last_convo = User.objects.get(pk = request.user.userprofile.lastConvo);
  for c in convos:
    tmp = User.objects.get(pk = c['fromUser'])
    new_messages = msgs.filter(isSeen = False)
    convo_list.append(tmp)


  # Now we check if any messages from a specific user has sent a new message
  # this will be used to highlight the cell in the sidebar
  for c in convo_list:
    mess = Message.objects.filter(toUser = request.user.pk).filter(fromUser = c.pk)
    m_new = mess.filter(isSeen = False)
    if m_new.count() > 0:
      c.hasNew = True
    else:
      c.hasNew = False
    m_date = mess.aggregate(Min('dateSent'))
    c.last_date = m_date['dateSent__min']


  c = {
          'last_convo': last_convo,
          'convo_list': convo_list,
          'sidebar': "pages/users/sidebars/messages.html",
          'title': last_convo.username,
          }
  return render(request, "pages/users/messages.html", c)



@login_required
def associates(request):
  associates = Associate.objects.filter(requested = request.user).exclude(dateAccepted = None).filter(dateRemoved = None)
  pending = Associate.objects.filter(requested = request.user).filter(dateAccepted = None).filter(dateRemoved = None)
  requests = Associate.objects.filter(requesting = request.user).filter(dateAccepted = None).filter(dateRemoved = None)
  pending_count = pending.count()
  print(associates)
  c = {
          'associates': associates,
          'pending': pending,
          'pending_count': pending_count,
          'requests': requests,
          'title': "Associates",
          }
  return render(request, "pages/users/associates.html", c)

@login_required
def remove_associate(request):
  if request.method == "GET":
    aID = request.GET['aID']
    a = Associate.objects.get(pk = aID)
    a.dateRemoved = datetime.date.today()
    a.save()

  return HttpResponseRedirect("/user/associates/")


@login_required
def accept_associate(request):
  if request.method == "GET":
    aID = request.GET['aID']
    a = Associate.objects.get(pk = aID)
    a.dateAccepted = datetime.date.today()
    a.save()

  return HttpResponseRedirect("/user/associates/")



@login_required
def projects(request):
  projects = Project.objects.filter(createdBy = request.user)
  c = {
          'title': "My Projects",
          'projects': projects, 
          }
  return render(request, "pages/users/projects.html", c)


@login_required
def requests(request):
  c = {
          'title': "Project Requests",
          }
  return render(request, "pages/users/requests.html", c)
# Create your views here.
