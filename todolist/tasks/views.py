from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse





class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"task.html",{
        "tasks": request.session["tasks"]
    })
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
           task = form.cleaned_data["task"]
           request.session["tasks"] +=[task]
           return HttpResponseRedirect(reverse("task"))
        else:
            return render(request,"add.html",{
                "form": form
            })
        
    return render(request,"add.html",{
        "form":NewTaskForm()
    })