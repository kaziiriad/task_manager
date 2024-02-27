
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import (
    View,
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    TemplateView
)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import CreateTaskForm, UpdateTaskForm
from guest_user.mixins import AllowGuestUserMixin

class HomeView(TemplateView):
    template_name = 'home.html'

class TaskListView(AllowGuestUserMixin, LoginRequiredMixin, ListView):

    model = Task
    template_name = 'tasks/task_list.html'
    login_url = reverse_lazy('login')
    context_object_name = 'task_list'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset
    

class TaskCreateView(LoginRequiredMixin, AllowGuestUserMixin, CreateView):


    model = Task
    form_class = CreateTaskForm
    login_url = reverse_lazy('login')

    def get_success_url(self) -> str:
        return reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TaskCreateView, self).form_valid(form)
    
    def form_invalid(self, form):
        print('form valid called')

        return self.render_to_response(
            self.get_context_data(form=form)
        )
    

class TaskUpdateView(LoginRequiredMixin, AllowGuestUserMixin, UpdateView):
    
    model = Task
    form_class = UpdateTaskForm
    #fields = ['title', 'description', 'due_date', 'priority', 'status']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully')
        return super(TaskUpdateView, self).form_valid(form)

class TaskStatusUpdateView(LoginRequiredMixin, AllowGuestUserMixin, View):

    def post(self, request):

        task_id = request.POST.get('task_id')
        status = request.POST.get('status')
        try:
            task = Task.objects.get(id=task_id)
            task.status = True if status == 'completed' else False
            task.save()
            return JsonResponse({'success' : True, 'status' : task.get_status_display() })
        except Task.DoesNotExist:
            return JsonResponse({'success' : False, 'error': 'Task not found'})
    


class TaskDetailView(LoginRequiredMixin, AllowGuestUserMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_details.html'
    login_url = reverse_lazy('login')
    

class TaskDeleteView(LoginRequiredMixin, AllowGuestUserMixin, DeleteView):
    
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDeleteView,self).form_valid(form)




