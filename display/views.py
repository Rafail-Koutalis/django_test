from django.template import loader
from django.http import HttpResponse
from add.models import Task

def display(request) :
    all_tasks = Task.objects.all()
    template = loader.get_template("display/display.html")
    context = {"all_tasks" : all_tasks,}
 
    return HttpResponse(template.render(context,request))

     