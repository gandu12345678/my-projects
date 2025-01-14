from django.shortcuts import render,redirect
from zai.models import Room,Message

def home(request):
    return render(request,"home.html")

def room(request,room):
    return render(request, 'room.html')

def checkview(request):
    room = request.POST['roomname']
    username = request.POST['username']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/'+ room + '/?username=' + username )
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+ room + '/?username=' + username )