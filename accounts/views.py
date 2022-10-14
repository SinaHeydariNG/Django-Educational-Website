from re import sub
from django.shortcuts import render , redirect , get_list_or_404 , HttpResponse
from .models import CustomUser , Messages , SavedCourses
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import MessageForm , UserForm
from main.models import SiteInfo , Socials
from courses.models import Courses

def register(request):
    information = SiteInfo.objects.last()
    socials = Socials.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        image = request.FILES['image']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request , 'This username has already been taken')
                return redirect('users:register')
            elif CustomUser.objects.filter(email=email):
                messages.error(request , 'This email has already been taken')
                return redirect('users:register')
            else:
                user = CustomUser.objects.create_user(first_name=first_name , last_name=last_name, username=username, email=email, password=password , image = image , birthday = birthday , address = address , phone_number = phone_number)    
                auth.login(request , user)
                return redirect('main:home')
    else:
        context = {
            "title" : "register",
            "information" : information,
            "socials" : socials
        }
        return render(request,'accounts/register.html' , context)




def login(request):
    information = SiteInfo.objects.last()
    socials = Socials.objects.all()
    if request.method ==  "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username , password)
        user = auth.authenticate(username=username , password=password)
        if user is not None:
            auth.login(request , user)  
            return redirect('main:home')
        else: 
            messages.error(request , 'Wrong username or password')
            return redirect('users:login')
    context = {
        "title" : "Login",
        "information" : information
        }
    return render(request , 'accounts/login.html' , context)



@login_required()
def logout(request):
    auth.logout(request)
    return redirect("main:home")

@login_required()
def dashboard(request):                         
    user = request.user             
    information = SiteInfo.objects.last()           
    socials = Socials.objects.all()         
    if Messages.objects.filter(user = user).exists():               
        user_message = Messages.objects.filter(user = user)         
    else:
        user_message = None    
    if SavedCourses.objects.filter(user = user).exists():
        saved_courses = SavedCourses.objects.get(user = user)
    else:
        saved_courses = None    
    context = {
        "title" : "Dashboard",
        "information" : information,
        "saved_courses" : saved_courses,
        "socials" : socials,
        "user_message" : user_message
    }
    return render(request , 'accounts/dashboard.html' , context)


@login_required()
def add_message(request):
    form = MessageForm()
    socials = Socials.objects.all()
    information = SiteInfo.objects.last()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            subject = form.cleaned_data['subject']
            user = request.user
            text = form.cleaned_data['text']
            new_message = Messages()
            new_message.title = title
            new_message.subject = subject
            new_message.user = user
            new_message.text = text
            new_message.save()
            return redirect("main:home")
        else:
            print("Not Valid")
            messages.error(request , form.errors)
            return redirect("users:message")    

    context = {
        "form" : form,
        "title" : "New Message",
        "information" : information,
        "socials" : socials
    }
    return render(request , 'accounts/message.html' , context)

@login_required()
def save_course(request , pk):
    this_course = Courses.objects.get(pk=pk)
    user = request.user
    socials = Socials.objects.all()
    if SavedCourses.objects.filter(user = user).exists():
        user_saved = SavedCourses.objects.get(user = user)
        if this_course in user_saved.courses.all():
            return redirect("users:dashboard")
        else:
            user_saved.courses.add(this_course)
            return redirect("users:dashboard")  
    else:
        user_saved = SavedCourses.objects.create(
            user = user
        )
        user_saved.save()
        user_saved.courses.add(this_course)
        return redirect("users:dashboard")  

def delete_course(request , pk):
    this_course = Courses.objects.get(pk=pk)
    user = request.user
    user_saved = SavedCourses.objects.get(user = user)
    user_saved.courses.remove(this_course)
    return HttpResponse("Deleted SuccessFully :)")

def update_profile(request):
    if request.method == "POST":
        user = request.user
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        if request.FILES:
            image = request.FILES['image']
            CustomUser.objects.update_or_create(  first_name = first_name , last_name = last_name , address = address , phone_number = phone_number , image = image )
            return redirect("users:dashboard")
        else:    
            CustomUser.objects.update_or_create( first_name = first_name , last_name = last_name , address = address , phone_number = phone_number) 
            return redirect("users:dashboard")   
    else:
        return redirect("users:dashboard")        


            


