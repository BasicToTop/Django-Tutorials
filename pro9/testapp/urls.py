from django.urls import path

from testapp.views import TaskCreateGenericView, TaskList, TaskListGeneric, task_list

urlpatterns = [
    # path('', task_list, name='task-list'),
    # path('', TaskList.as_view(), name='task-list'),
    path('', TaskListGeneric.as_view(), name='task-list'),
    path('create/', TaskCreateGenericView.as_view(), name='task-create'),
]
