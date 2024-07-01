from django.shortcuts import render
import datetime
# Create your views here.
def new(request):
    now=datetime.datetime.now()
    return render(request,"newnewnew.html",{
        "newyear": now.month==1 & now.day==1
})
