from django import forms
from .models import Task

# class DateInput(forms.DateInput):
#     input_type = 'date'

class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'priority')
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

class UpdateTaskForm(forms.ModelForm):
     
     class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'priority', 'status')
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }