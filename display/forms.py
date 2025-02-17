from django.forms import ModelForm
from add.models import Task

class UpdatecompletedForm(ModelForm) :
    class Meta :
        model = Task
        fields = ('completed',)