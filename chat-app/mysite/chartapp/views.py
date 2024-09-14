from django.shortcuts import render
from .models import ChartRoom,ChatMessage
# Create your views here.
def index(request):

    chartooms=ChartRoom.objects.all()
    return render(request,'chartapp/index.html',{'chartooms':chartooms})

def chartroom(request,slug):
    chartroom=ChartRoom.objects.get(slug=slug)
    messages=ChatMessage.objects.filter(room=chartroom)[0:30]
    return render(request,'chartapp/room.html',{'chartroom':chartroom,'messages':messages})