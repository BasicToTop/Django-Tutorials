from django.shortcuts import render
from testapp.models import Employee
from testapp.forms import EmployeeForm
# Create your views here.


def employee_list(request):
    form = EmployeeForm()
    first_name = request.GET.get('first_name')
    email = request.GET.get('email')
    if first_name:
        records = Employee.objects.filter(first_name__iexact=first_name).order_by('first_name')
    elif email:
        records = Employee.objects.filter(email__iexact=email).order_by('first_name')
    else:
        records = Employee.objects.all().order_by('first_name') # Fetch all employee records
    context = {'employees': records, 'form': form}
    template_name = 'testapp/employee_list.html'
    return render(request, template_name, context)