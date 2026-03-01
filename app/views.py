from django.contrib.auth import authenticate,login,logout
from django.http import request
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import *
from .models import *
import datetime

daDate = datetime.datetime.now()

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.method == "POST":
        title = request.POST["title"]
        contents = request.POST["contents"]
        status = request.POST["status"]
        rating = request.POST["rating"]
        noteType = request.POST["noteType"]
        memster = request.POST["memster"]
        theDate = daDate.strftime("%d %b %Y - %I:%M %p")

        task = Task(user=request.user.username,title=title,contents=contents,status=status,rating=rating,noteType=noteType,memster=memster,theDate=theDate)
        task.save()

    return render(request,"app/index.html",{
        "taskProf" : Task.objects.all().filter(user=request.user.username,noteType="professional"),
        "taskper" : Task.objects.all().filter(user=request.user.username,noteType="personal"),
        "tasksAll" : Task.objects.all().filter(user=request.user.username),
        "publicTasks" : Task.objects.all().filter(memster="public"),
        "users" : User.objects.all(),
    })

def userProfile(request,user_id):
    user = User.objects.get(pk=user_id)
    return render(request,"app/userprofile.html",{
        "user" : user,
    })

def userMemster(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "app/userMemster.html",{
        "user" : user,
        "memsters" : Task.objects.all().filter(user=user.username,memster="public"),
    })


def loginView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
        
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"app/login.html",{
                "message" : "Form is invalid",
                "messageColor" : "red"
            })

    return render(request,"app/login.html",{
        "message" : "Welcome Back!",
        "messageColor" : "limegreen"
    })

def registerView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request,"app/register.html",{
                "form" : NewUserForm(request.POST),
                "message" : "Something is wrong!",
                "messageColor" : "red",
            })

    return render(request,"app/register.html",{
        "form" : NewUserForm,
        "message" : "Welcome To Memories!",
        "messageColor" : "green",
    })

def logoutView(request):
    logout(request)
    return render(request,"app/login.html",{
        "message" : "Logged Out!",
        "messageColor" : "red",
    })

def noteView(request,task_id):
    task = Task.objects.get(pk=task_id)
    return render(request,"app/note.html",{
        "task" : task,
    })

def deleteTask(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse("index"))

def editTaskView(request,task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == "POST":
        title = request.POST["title"]
        contents = request.POST["contents"]
        status = request.POST["status"]
        rating = request.POST["rating"]
        noteType = request.POST["noteTypeEdit"]
        memster = request.POST["memster"]

        Task.objects.filter(pk=task_id).update(title=title,contents=contents,status=status,rating=rating,noteType=noteType,memster=memster)

        return HttpResponseRedirect(reverse("index"))

    return render(request,"app/editTask.html",{
        "task" : task,
    })
