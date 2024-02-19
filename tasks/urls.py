from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskStatusUpdateView,
    TaskDeleteView,
    HomeView
    # update_task_status
)

from accounts_manager import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('list_task/', TaskListView.as_view(), name='task-list'),
    path('create_task/', TaskCreateView.as_view(), name='task-create'),
    path('update_task/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('update_task_status/', TaskStatusUpdateView.as_view(), name='task-status-update'),
    path('detail_task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('delete_task/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    # path('update_task_status/<int:id>', update_task_status, name='task-status'),

]
