from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room,Message

@login_required
def room(request):

   rooms=Room.objects.all()
   context={
       "rooms":rooms
   }
   return render(request,"rooms.html",context)

@login_required
def room_detail(request,slug):

   room=Room.objects.get(slug=slug)
   messages=Message.objects.filter(room=room)[0:25]
   context={
       "room":room,
       "messages":messages
   }
   return render(request,"room.html",context)
