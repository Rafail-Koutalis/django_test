from django.forms import ModelForm
from add.models import Task
from django import forms

class TaskFormSearch(ModelForm) :
    def __init__(self,*args,**kwargs) :
        super().__init__(*args,**kwargs)
        for field in self.fields :
            self.fields[str(field)].widget.attrs.update({'placeholder' : f'Enter the task name here.','rows' : 1,'autofocus':'autofocus'})
    class Meta :
        model = Task
        fields = ('task_name',)


     

class TaskFormDelete(ModelForm) :
 
    def __init__(self,*args,**kwargs) :
        super().__init__(*args,**kwargs)
        for field in self.fields :
            if str(field) == 'task_' :
                self.fields[str(field)].label=''
            self.fields[str(field)].widget.attrs.update({'placeholder' : f'Enter the {field} here.'})
            
    class Meta :
        model = Task
        fields = ('task_name',)
