from django.shortcuts import render , redirect , get_list_or_404 , HttpResponse 
from courses.models import Category , Courses
from accounts.models import Messages 
from accounts.forms import MessageForm
from .models import SiteInfo , Socials
# Create your views here.

def home(request):
    course_cat = Category.objects.all()
    courses = Courses.objects.all()
    last_course = Courses.objects.last()
    activate_messages = Messages.objects.filter(activate = True)
    information = SiteInfo.objects.last()
    message_form = MessageForm()
    socials = Socials.objects.all()
    context = {
        "title" : "HOME",
        "course_cat" : course_cat,
        "courses" : courses,
        "last_course" : last_course,
        "activate_messages" : activate_messages,
        "message_form" : message_form,
        "information" : information,
        "socials" : socials
    }
    return render(request , 'main/home.html' , context)