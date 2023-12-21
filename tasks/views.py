from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView
)
from .forms import CreateTaskForm
import logging


logger = logging.getLogger(__name__)

def index(request):

    return render(request, 'home.html')

class TaskListView(LoginRequiredMixin, ListView):

    model = Task
    template_name = 'tasks/task_list.html'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset
    
    

# class TaskCreateView(LoginRequiredMixin, CreateView):


#     model = Task
#     form_class = CreateTaskForm
#     login_url = reverse_lazy('login')

#     def get_success_url(self) -> str:
#         return reverse_lazy('task-list')
    
#     def form_valid(self, form):
#         print('form valid called')

#         form.instance.user = self.request.user
#         form.save()
#         return super(TaskCreateView, self).form_valid(form)
    
#     def form_invalid(self, form):
#         print('form valid called')

#         return self.render_to_response(
#             self.get_context_data(form=form)
#         )
    
#     #fields = ['title', 'description', 'due_date', 'priority']
@login_required
def create_task(request):

    if request.method == 'POST':

        form = CreateTaskForm(request.POST)

        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()

            return redirect('task-list')
        
    form = CreateTaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})


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

