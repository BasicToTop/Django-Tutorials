from django.contrib import admin
from testapp.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'task_name', 'status', 'assigned_by', 'assigned_to', 'assigned_date', 'deadline')
    search_fields = ('task_id', 'task_name', 'status')
    list_filter = ('status', 'assigned_by', 'assigned_to')

admin.site.register(Task, TaskAdmin)