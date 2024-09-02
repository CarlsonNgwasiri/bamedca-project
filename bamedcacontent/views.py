from django.http import response
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings


from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView, TemplateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView, View)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.core.mail import send_mail
# Create your views here.


def home(request):
    contact=ContactModel.objects.all()
    context={
        'contact':contact
    }
    return render(request, 'home.html',context=context)

def about(request):
    about=AboutModel.objects.all()
    exco = ExecutiveModel.objects.all()
    contact=ContactModel.objects.all()
    context={
        'about':about,
        'exco':exco,
        'contact':contact
    }
    return render(request, 'about.html',context=context)

def branch(request):
    branch=BranchModel.objects.all()
    contact=ContactModel.objects.all()
    context={
        'branch':branch,
        'contact':contact
    }
    return render(request, 'branch.html',context=context)

def projects(request):
    projects = ProjectModel.objects.all()
    contact=ContactModel.objects.all()
    context={
        'contact':contact,
        'projects':projects
    }
    return render(request, 'projects.html',context=context)

def events(request):
    events = EventModel.objects.all()
    contact=ContactModel.objects.all()
    context={
        'contact':contact,
        'events':events
    }
    return render(request, 'events.html',context=context)

def contact(request):
    contact=ContactModel.objects.all()
    context={
        'contact':contact
    }
    return render(request, 'contact.html',context=context)

def branchDetails(request,ID):
    object=BranchModel.objects.get(id=ID)
    contact=ContactModel.objects.all()
    quarters = QuaterModel.objects.filter(branch=object)
    context={
        'objects':object,
        'contact':contact,
        'quarters':quarters
    }
    return render(request,'branch-details.html',context=context)

def aboutDetails(request,ID):
    object=AboutModel.objects.get(id=ID)
    contact=ContactModel.objects.all()
    context={
        'objects':object,
        'contact':contact
    }
    return render(request, 'about-details.html',context=context)


def projectDetails(request,ID):
    object=ProjectModel.objects.get(id=ID)
    contact=ContactModel.objects.all()
    print(object)
    context={
        'objects':object,
        'contact':contact
    }
    return render(request,'project-details.html',context=context)

def eventsDetails(request,ID):
    object=ProjectModel.objects.get(id=ID)
    contact=ContactModel.objects.all()
    print(object)
    context={
        'objects':object,
        'contact':contact
    }
    return render(request,'events-details.html',context=context)
    