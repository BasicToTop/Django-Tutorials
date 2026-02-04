from django.shortcuts import render
from testapp.models import Employee
from testapp.forms import EmployeeForm
# Create your views here.


def employee_list(request):
    form = EmployeeForm()
    first_name = request.GET.get('first_name')
    email = request.GET.get('email')
    salary = request.GET.get('salary')
    from_salary = request.GET.get('from_salary')
    to_salary = request.GET.get('to_salary')
    if first_name:
        records = Employee.objects.filter(first_name__icontains=first_name).order_by('first_name')
    elif email:
        records = Employee.objects.filter(email__iexact=email).order_by('first_name')
    elif salary:
        # records = Employee.objects.filter(salary__gt=salary)
        # records = Employee.objects.filter(salary__gte=salary)
        # records = Employee.objects.filter(salary__lt=salary)
        records = Employee.objects.filter(salary__lte=salary)
    elif from_salary and to_salary:
        records = Employee.objects.filter(salary__range=(from_salary, to_salary))
    else:
        records = Employee.objects.all().order_by('first_name') # Fetch all employee records
    context = {'employees': records, 'form': form}
    template_name = 'testapp/employee_list.html'
    return render(request, template_name, context)