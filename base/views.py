from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id':1, 'name': 'Lets learn python'},
    {'id':1, 'name': 'Design my webpage'},
    {'id':1, 'name': 'C++ learning'}
]

def home(request):
    context = { 'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    return render(request, 'base/room.html')