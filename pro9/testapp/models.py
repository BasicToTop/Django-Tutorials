from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    task_id = models.CharField(max_length=100, primary_key=True)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    TASK_STATUS = (('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'))
    status = models.CharField(max_length=50, choices=TASK_STATUS, default='pending')
    assigned_date = models.DateField()
    deadline = models.DateField()
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_to_tasks')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task_id