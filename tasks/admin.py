from django.contrib import admin
from .models import Task, Image
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('title', 'priority', 'status',)
    list_filter = ('priority', 'status',)
    search_fields = ('task__title',)
    ordering = ('priority',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ('images',)
    list_filter = ('belongs_to',)
    search_fields = ('belongs_to__title', 'images__filename',)