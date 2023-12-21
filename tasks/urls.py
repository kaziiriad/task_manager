from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
)

from accounts_manager import views


urlpatterns = [
    path('', index, name='home'),
    path('list_task/', TaskListView.as_view(), name='task-list'),
    path('create_task/', TaskCreateView.as_view(), name='task-create'),
    path('update_task/<int:pk>', TaskCreateView.as_view(), name='task-update'),

]
