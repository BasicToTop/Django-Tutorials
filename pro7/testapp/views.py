from django.shortcuts import render
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.db.models import Q
# Create your views here.


def employee_list(request):
    form = EmployeeForm()
    first_name = request.GET.get('first_name')
    email = request.GET.get('email')
    salary = request.GET.get('salary')
    from_salary = request.GET.get('from_salary')
    to_salary = request.GET.get('to_salary')
    print('first_name ',first_name)
    records = Employee.objects.all().order_by('first_name')  # Fetch all employee records   
    if first_name:
        records = Employee.objects.filter(~Q(first_name__istartswith=first_name)).order_by('first_name')
    # if first_name and salary:
    #     records = Employee.objects.filter(
    #                  Q(first_name__startswith=first_name) & Q(salary__lt=salary))
    # if first_name and salary:
    #     records = Employee.objects.filter(
    #                  Q(first_name__startswith=first_name) | Q(salary__gt=salary)) 


    # records = Employee.objects.filter(
    #         Q(first_name__startswith=first_name) & Q(salary__lt=salary))

    # if first_name is not None and salary is None:
    #     records = Employee.objects.filter(
    #         first_name__istartswith=first_name).order_by('first_name')
    # elif email:
    #     records = Employee.objects.filter(
    #         email__iexact=email).order_by('first_name')
    # elif salary is not None and first_name is None:
    #     # records = Employee.objects.filter(salary__gt=salary)
    #     # records = Employee.objects.filter(salary__gte=salary)
    #     # records = Employee.objects.filter(salary__lt=salary)
    #     records = Employee.objects.filter(salary__lte=salary)
    # elif from_salary and to_salary:
    #     records = Employee.objects.filter(
    #         salary__range=(from_salary, to_salary))
    # elif first_name and salary:
    #     records = Employee.objects.filter(
    #         Q(first_name__startswith=first_name) & Q(salary__lt=salary))
    # else:
    #     records = Employee.objects.all().order_by(
    #         'first_name')  # Fetch all employee records
    context = {'employees': records, 'form': form}
    template_name = 'testapp/employee_list.html'
    return render(request, template_name, context)
