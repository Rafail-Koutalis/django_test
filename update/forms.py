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


     

class TaskFormUpdate(ModelForm) :
    description = forms.CharField(widget=forms.Textarea(attrs={'rows' : 6,'autofocus':'autofocus'}))
    def __init__(self,*args,**kwargs) :
        super().__init__(*args,**kwargs)
        for field in self.fields :
            if str(field) == 'description' :
                self.fields[str(field)].label=''
            self.fields[str(field)].widget.attrs.update({'placeholder' : f'Enter the {field} here.'})
            
    class Meta :
        model = Task
        fields = ('description','completed')
