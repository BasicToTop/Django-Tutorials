from django.shortcuts import render, redirect
from mainapp.forms import CountryForm, StateForm, GenderForm, QualificationForm, UniversityForm, StudentForm
# Create your views here.


def home(request):
    return render(request, 'mainapp/home.html', context={})


def country(request):
    if request.method == 'GET':
        # write the logic to display the form for clients
        form = CountryForm()
        template_name = 'mainapp/country.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        # write the logic to get the form data from clients and validate then save into database table.
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country')
        else:
            template_name = 'mainapp/country.html'
            context = {'form': form}
            return render(request, template_name, context)


def state(request):
    if request.method == 'GET':
        # write the logic to display the form for clients
        form = StateForm()
        template_name = 'mainapp/state.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        # write the logic to get the form data from clients and validate then save into database table.
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('state')
        else:
            template_name = 'mainapp/state.html'
            context = {'form': form}
            return render(request, template_name, context)


def qualification(request):
    if request.method == 'GET':
        # write the logic to display the form for clients
        form = QualificationForm()
        template_name = 'mainapp/qualification.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        # write the logic to get the form data from clients and validate then save into database table.
        form = QualificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qualification')
        else:
            template_name = 'mainapp/qualification.html'
            context = {'form': form}
            return render(request, template_name, context)


def gender(request):
    if request.method == 'GET':
        # write the logic to display the form for clients
        form = GenderForm()
        template_name = 'mainapp/gender.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        # write the logic to get the form data from clients and validate then save into database table.
        form = GenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gender')
        else:
            template_name = 'mainapp/gender.html'
            context = {'form': form}
            return render(request, template_name, context)


def university(request):
    if request.method == 'GET':
        # write the logic to display the form for clients
        form = UniversityForm()
        template_name = 'mainapp/university.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        # write the logic to get the form data from clients and validate then save into database table.
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('university')
        else:
            template_name = 'mainapp/university.html'
            context = {'form': form}
            return render(request, template_name, context)


def student(request):
    if request.method == 'GET':
        # write the logic to display the form for clients
        form = StudentForm()
        template_name = 'mainapp/student.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        # write the logic to get the form data from clients and validate then save into database table.
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
        else:
            template_name = 'mainapp/student.html'
            context = {'form': form}
            return render(request, template_name, context)
