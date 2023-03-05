from django.shortcuts import render, redirect
from .models import Item
# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def add(request):
    if(request.method =="POST"):
        name = request.POST.get('title')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)   
        return redirect('/')     
