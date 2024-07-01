from django.shortcuts import render

tasks = ["fat","thin","motey"]
# Create your views here.
def tsk(request):
    return render ( request, "yes.html" ,{
        "tasks": tasks
    })