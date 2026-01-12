from django.shortcuts import render, redirect
from mainapp.forms import CountryForm, StateForm, GenderForm, QualificationForm, UniversityForm, StudentForm
# Create your views here.


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

