from django.shortcuts import render, redirect
from mainapp.forms import CountryForm, StateForm, GenderForm, QualificationForm, UniversityForm, StudentForm
from mainapp.models import Country, Gender, Qualification, State, Student, University
# Create your views here.


def home(request):
    country_count = Country.objects.all().count()
    state_count = State.objects.all().count()
    qualification_count = Qualification.objects.all().count()
    gender_count = Gender.objects.all().count()
    university_count = University.objects.all().count()
    student_count = Student.objects.all().count()
    print('country_count ', country_count)
    print('state_count ', state_count)
    print('qualification_count ', qualification_count)
    context = {'country_count': country_count, 'state_count': state_count,
               'qualification_count': qualification_count,
               'gender_count': gender_count,
               'university_count': university_count,
               'student_count': student_count}
    return render(request, 'mainapp/home.html', context)


def country_list(request):
    countries = Country.objects.all().order_by('country_name')
    context = {'countries': countries}
    template_name = 'mainapp/country_list.html'
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
            return redirect('country_list')
        else:
            template_name = 'mainapp/country.html'
            context = {'form': form}
            return render(request, template_name, context)


def country_delete(request, pk):
    country = Country.objects.get(pk=pk)
    country.delete()
    return redirect('country_list')


def country_edit(request, pk):
    country = Country.objects.get(pk=pk)
    if request.method == 'GET':
        form = CountryForm(instance=country)
        template_name = 'mainapp/country.html'
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_list')
        else:
            template_name = 'mainapp/country.html'
            context = {'form': form}
            return render(request, template_name, context)


def country_detail(request, pk):
    country = Country.objects.get(pk=pk)
    context = {'country': country}
    template_name = 'mainapp/country_detail.html'
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
