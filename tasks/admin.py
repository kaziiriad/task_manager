from django.contrib import admin
from .models import Task, Image
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'priority', 'status')
    ordering = ('priority')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ('images')