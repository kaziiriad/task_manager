from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    PRIORITY = [
        (0, "Null"),
        (1, "High"),
        (2, "Medium"),
        (3, "Low")
    ]
    COMPLETION_CHOICES = [
        (True, "Completed"),
        (False, "Incomplete")
    ] 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(choices=PRIORITY, default=0)
    status = models.CharField(choices=COMPLETION_CHOICES, default=False)

    def __str__(self) -> str:
        return f'Task {self.title} with a {self.priority} priority, to be completed before {self.due_date}.'
    
    class Meta:
        verbose_name = 'Task'
        ordering = ['created_at', 'due_date', 'priority', 'status']


