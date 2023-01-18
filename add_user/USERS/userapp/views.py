from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404


## views.py 

from .forms import *
from .models import *

"""
def home(request):
    form = BookForm()
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "home.html",{'form':form}) """

def home(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        your_object = form.save(commit=False)
        your_object.created_by = request.user
        your_object.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'home.html', context) 
