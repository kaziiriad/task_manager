from django.urls import path
from .views import (
    index,
    TaskListView,
    create_task,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
)

from accounts_manager import views


urlpatterns = [
    path('', index, name='home'),
    path('list_task/', TaskListView.as_view(), name='task-list'),
    path('create_task/', create_task, name='task-create'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('detail_task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),

]
