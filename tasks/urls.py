from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    # update_task_status
)

from accounts_manager import views


urlpatterns = [
    path('', index, name='home'),
    path('list_task/', TaskListView.as_view(), name='task-list'),
    path('create_task/', TaskCreateView.as_view(), name='task-create'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('detail_task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
    # path('update_task_status/<int:id>', update_task_status, name='task-status'),

]
