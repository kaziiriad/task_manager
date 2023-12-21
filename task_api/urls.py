from django.urls import path
from . import views


urlpatterns = [
    path('all', views.get_all_task, name='all-task'),
    path('task/<int:pk>', views.get_task, name='get-task'),
    path('create/', views.create_task),
    path('update/<int:pk>', views.update_task),
    path('delete/<int:pk>', views.delete_task, name='get-task'),

]
