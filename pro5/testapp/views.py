from django.shortcuts import render, redirect
from testapp.forms import EmployeeRegistrationForm
# Create your views here.


def employee_registration(request):
    if request.method == 'GET':
        form = EmployeeRegistrationForm()
        template_name = 'testapp/employee_registration.html'
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():  # this is to validate the form
            # write code to same the data into database, crospnding table
            form.save()
            return redirect('employee_registration')

        else:
            template_name = 'testapp/employee_registration.html'
            context = {'form': form}
            return render(request, template_name, context)
