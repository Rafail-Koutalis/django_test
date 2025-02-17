from django.shortcuts import render
from .forms import TaskForm
from .models import Task
from django.contrib import messages

def add_task(request) :
    form = TaskForm()
    if request.method == "POST" :
        form = TaskForm(request.POST)
        if form.is_valid() :
            form.save()
            form = TaskForm()
            messages.success(request, 'Task added succesfully! Feel free to procced as you like. ')         
    else :
        form = TaskForm()
        
    context = {'form' : form,}
    return render(request,'add/add.html',context)  
       