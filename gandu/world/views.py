from django.shortcuts import render
from .models import Flight
# Create your views here.
def quack(request):
    return render(request,"index.html",{
        "flights":Flight.objects.all()
    })
