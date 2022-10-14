from django.shortcuts import render , get_list_or_404 , HttpResponse , redirect ,get_object_or_404
from .models import Courses , Category , Episodes
from django.core.paginator import Paginator
from main.models import SiteInfo , Socials
from django.core.paginator import Paginator
# Create your views here.

def list(request):
    socials = Socials.objects.all()
    information = SiteInfo.objects.last()
    courses = Courses.objects.all()
    course_paginator = Paginator(courses , 2)
    get_page = request.GET.get('page')
    courses = course_paginator.get_page(get_page)

    context = {
        "title" : "List",
        "courses" : courses,
        "information" : information,
        "socials" : socials  
    }
    return render(request , 'courses/list.html' , context)

def detail(request , slug):
    socials = Socials.objects.all()
    information = SiteInfo.objects.last()
    course = get_object_or_404(Courses , slug = slug)
    title = course.title
    context = {
        "title" : title,
        "course" : course,
        "information" : information,
        "socials" : socials
    }
    return render(request , 'courses/detail.html' , context)

def episode(request , pk , slug):
    socials = Socials.objects.all()
    information = SiteInfo.objects.last()
    episode = get_object_or_404(Episodes , pk=pk)
    course = get_object_or_404(Courses , slug = slug)
    title = course.title
    context = {
        "title" : title,
        "course" : course,
        "episode" : episode,
        "information" : information,
        "socials" : socials
    }
    return render(request , 'courses/detail.html' , context)

# Saved Functionality

# Saved Functionality