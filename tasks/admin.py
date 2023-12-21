from django.contrib import admin
from .models import Task
# Register your models here.



class TaskAdmin(admin.ModelAdmin):

    list_display = ('title', 'priority', 'status',)
    list_filter = ('priority', 'status',)
    search_fields = ('task__title',)
    ordering = ('priority',)

admin.site.register(Task, TaskAdmin)