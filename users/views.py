from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from users.models import UserProfile


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
          'show_sidebar': True,
          'sidebar': 'basics/sidebar.html',
          }
  return render(request, "pages/users/profile.html", c)


# Create your views here.
