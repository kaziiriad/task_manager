from typing import Any
from django.db.models.query import _BaseQuerySet, QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView
)
from .forms import CreateTaskForm

def index(request):

    return render(request, 'home.html')

class TaskListView(LoginRequiredMixin, ListView):

    model = Task
    template_name = 'tasks/task_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Task.objects.filter(user=self.request.user)
        return queryset
    
    

class TaskCreateView(LoginRequiredMixin, CreateView):

    model = Task
    form_class = CreateTaskForm
    login_url = reverse_lazy('login')
    #fields = ['title', 'description', 'due_date', 'priority']



class TaskUpdateView(LoginRequiredMixin, UpdateView):
    
    model = Task
    form_class = CreateTaskForm
    #fields = ['title', 'description', 'due_date', 'priority', 'status']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    login_url = reverse_lazy('login')


    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully')
        return super(TaskUpdateView, self).form_valid(form)
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_details.html'
    login_url = reverse_lazy('login')



class TaskDeleteView(LoginRequiredMixin, DeleteView):
    
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
    login_url = reverse_lazy('login')

