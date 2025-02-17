from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import TaskFormSearch, TaskFormUpdate
from add.models import Task


def search_task_2(request):
    form = TaskFormSearch()  # Initialize an empty form
    if request.method == 'POST':
        form = TaskFormSearch(request.POST or None)
        task_name = request.POST.get('task_name',)  # Get task_name from URL parameters
        if task_name:
            task_instance = Task.objects.filter(task_name=task_name).first()  # Query based on task_nam
            if task_instance:
                return redirect('updatetask',task_instance)
            else: 
                messages.error(request, 'No task found with that name. Keep searching.')
                form = TaskFormSearch()
                context = {'form' : form}
                return render(request, 'update/search_task_2.html', context)
    
    context = {'form' : form}
    return render(request, 'update/search_task_2.html', context)


 
def updatetask(request, task_name):
    task = Task.objects.get(task_name = task_name)
    form = TaskFormUpdate(instance=task)
    
    if request.method == "POST":
        form = TaskFormUpdate(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated succesfully! Feel free to procced as you like. ')   
            return redirect('search_task_2')
    
    context = {'form':form,}
    return render(request, 'update/search_task_2.html', context)
    
    
  