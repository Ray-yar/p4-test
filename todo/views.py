from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.
def home(request):
    form = ItemForm()
    context = {
        'form' : form
    }
    return render(request, 'todo/home.html', context)

def add(request):
    if(request.method =="POST"):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')     
