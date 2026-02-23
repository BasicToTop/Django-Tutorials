from django.shortcuts import render
from testapp.models import Task
from django.views import View
from django.views.generic import ListView, CreateView
# Create your views here.


def task_list(request):
    obj = Task.objects.all()
    template_name = 'testapp/index.html'
    context = {'tasks': obj}
    return render(request, template_name, context)


class TaskList(View):
    def get(self, request):
        obj = Task.objects.all()
        template_name = 'testapp/index.html'
        context = {'tasks': obj}
        return render(request, template_name, context)

# Generic Class Based Views (GCBV) can be used to simplify the code further, but for now, this is a basic implementation of both function-based and class-based views


class TaskListGeneric(ListView):
    model = Task


class TaskCreateGenericView(CreateView):
    model = Task
    fields = '__all__'
