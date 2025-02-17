from django.forms import ModelForm,TextInput,CharField
from .models import Task
from django import forms

class TaskForm(ModelForm) :
    description = forms.CharField(widget=forms.Textarea(attrs={'rows' : 6}))
    task_name = forms.CharField(widget=TextInput(attrs={'autofocus' : 'autofocus'}))
    class Meta :
        model = Task
        fields = ['task_name','description']  

    def __init__(self,*args,**kwargs) :
        super().__init__(*args,**kwargs)
        for field in self.fields :
            self.fields[str(field)].label=''
            self.fields[str(field)].widget.attrs.update({'placeholder' : f'Enter the {field} here.'})
 