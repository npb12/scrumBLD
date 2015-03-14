from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from users.models import UserProfile, Friend


def register(request):
  if request.method == 'POST':
    print("posting")
    form = UserCreationForm(request.POST)
    if form.is_valid():
      print("is valid")
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
def profile(request):
  c = {
          'title': "Profile",
          }
  return render(request, "pages/users/profile.html", c)


@login_required
def messages(request):
  
  lst = ['Hello'] * 50

  c = {
          'lst': lst, 
          'sidebar': "pages/users/sidebars/messages.html",
          'title': "Messages",
          }
  return render(request, "pages/users/messages.html", c)


@login_required
def friends(request):
  friends = Friend.objects.all()
  friend_count = friends.count()
  users = User.objects.all()
  c = {
          'sidebar': "pages/users/sidebars/friends.html",
          'title': "Friends",
          'friends': friends,
          'friend_count': friend_count,
          'users':users,
          }
  return render(request, "pages/users/friends.html", c)


@login_required
def projects(request):
  c = {
          'title': "Projects",
          }
  return render(request, "pages/users/projects.html", c)


@login_required
def requests(request):
  c = {
          'title': "Project Requests",
          }
  return render(request, "pages/users/requests.html", c)
# Create your views here.
