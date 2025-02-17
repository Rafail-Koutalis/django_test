from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import TaskFormSearch, TaskFormDelete
from add.models import Task

def search_task(request):
    form = TaskFormSearch()  # Initialize an empty form
    if request.method == 'POST':
        form = TaskFormSearch(request.POST or None)
        task_name = request.POST.get('task_name',)  # Get task_name from URL parameters
        if task_name and task_name == 'all' :
            return redirect('deletetask',task_name='all')
        elif task_name :
            task_instance = Task.objects.filter(task_name=task_name).first()  # Query based on task_nam
            if task_instance:
                return redirect('deletetask',task_instance)
            else: 
                messages.error(request, 'No task found with that name. Keep searching.')
                form = TaskFormSearch()
                context = {'form' : form}
                return render(request, 'delete/search_task.html', context)
    
    context = {'form' : form}
    return render(request, 'delete/search_task.html', context)



def deletetask(request, task_name):
    if task_name == 'all' :
        Task.objects.all().delete()
        messages.success(request, 'All tasks deleted succesfully! Feel free to procced as you like. ')   
        return redirect('search_task')
    else :
        task = Task.objects.get(task_name = task_name)
        form = TaskFormDelete(instance=task)
        
        if request.method == "POST":
            form = TaskFormDelete(request.POST, instance=task)
            if form.is_valid():
                Task.objects.filter(task_name=task).delete()
                messages.success(request, 'Task deleted succesfully! Feel free to procced as you like. ')   
                return redirect('search_task')
    
    context = {'form':form,'task' : task}
    return render(request, 'delete/delete.html', context)