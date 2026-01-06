from django.shortcuts import render, redirect
from testapp.forms import EmployeeRegistrationForm, ContactInformationForm
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


def contact_info_create(request):
    if request.method == 'GET':
        form = ContactInformationForm()
        template_name = 'testapp/contact_info_create.html'
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == 'POST':
        form = ContactInformationForm(request.POST)
        if form.is_valid():
            '''
            Its runs only when form data is valid..
            '''
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email_address = form.cleaned_data['email_address']
            contact_info = {
                'full_name': full_name,
                'phone_number': phone_number,
                'email_address': email_address
            }
            print('contact_info ', contact_info)
            return redirect('contact_info_create')
        else:
            '''
            Its runs only when form data is not valid.
            '''
            

