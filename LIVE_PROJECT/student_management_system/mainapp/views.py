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


# ================= STATE VIEWS =================

def state_list(request):
    states = State.objects.all().order_by('state_name')
    context = {'states': states}
    template_name = 'mainapp/state_list.html'
    return render(request, template_name, context)


def state(request):
    if request.method == 'GET':
        form = StateForm()
        template_name = 'mainapp/state.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('state_list')
        else:
            template_name = 'mainapp/state.html'
            context = {'form': form}
            return render(request, template_name, context)


def state_delete(request, pk):
    state = State.objects.get(pk=pk)
    state.delete()
    return redirect('state_list')


def state_edit(request, pk):
    state = State.objects.get(pk=pk)
    if request.method == 'GET':
        form = StateForm(instance=state)
        template_name = 'mainapp/state.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            form.save()
            return redirect('state_list')
        else:
            template_name = 'mainapp/state.html'
            context = {'form': form}
            return render(request, template_name, context)


def state_detail(request, pk):
    state = State.objects.get(pk=pk)
    context = {'state': state}
    template_name = 'mainapp/state_detail.html'
    return render(request, template_name, context)
# ================= END STATE VIEWS =================

# ================= QUALIFICATION VIEWS =================


def qualification_list(request):
    qualifications = Qualification.objects.all().order_by('name')
    context = {'qualifications': qualifications}
    template_name = 'mainapp/qualification_list.html'
    return render(request, template_name, context)


def qualification(request):
    if request.method == 'GET':
        form = QualificationForm()
        template_name = 'mainapp/qualification.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qualification_list')
        else:
            template_name = 'mainapp/qualification.html'
            context = {'form': form}
            return render(request, template_name, context)


def qualification_delete(request, pk):
    qualification = Qualification.objects.get(pk=pk)
    qualification.delete()
    return redirect('qualification_list')


def qualification_edit(request, pk):
    qualification = Qualification.objects.get(pk=pk)
    if request.method == 'GET':
        form = QualificationForm(instance=qualification)
        template_name = 'mainapp/qualification.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = QualificationForm(request.POST, instance=qualification)
        if form.is_valid():
            form.save()
            return redirect('qualification_list')
        else:
            template_name = 'mainapp/qualification.html'
            context = {'form': form}
            return render(request, template_name, context)


def qualification_detail(request, pk):
    qualification = Qualification.objects.get(pk=pk)
    context = {'qualification': qualification}
    template_name = 'mainapp/qualification_detail.html'
    return render(request, template_name, context)

# ================= GENDER VIEWS =================


def gender_list(request):
    genders = Gender.objects.all().order_by('name')
    context = {'genders': genders}
    template_name = 'mainapp/gender_list.html'
    return render(request, template_name, context)


def gender(request):
    if request.method == 'GET':
        form = GenderForm()
        template_name = 'mainapp/gender.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = GenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gender_list')
        else:
            template_name = 'mainapp/gender.html'
            context = {'form': form}
            return render(request, template_name, context)


def gender_delete(request, pk):
    gender = Gender.objects.get(pk=pk)
    gender.delete()
    return redirect('gender_list')


def gender_edit(request, pk):
    gender = Gender.objects.get(pk=pk)
    if request.method == 'GET':
        form = GenderForm(instance=gender)
        template_name = 'mainapp/gender.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = GenderForm(request.POST, instance=gender)
        if form.is_valid():
            form.save()
            return redirect('gender_list')
        else:
            template_name = 'mainapp/gender.html'
            context = {'form': form}
            return render(request, template_name, context)


def gender_detail(request, pk):
    gender = Gender.objects.get(pk=pk)
    context = {'gender': gender}
    template_name = 'mainapp/gender_detail.html'
    return render(request, template_name, context)


# ================= UNIVERSITY VIEWS =================

def university_list(request):
    universities = University.objects.all().order_by('uc_name')
    context = {'universities': universities}
    template_name = 'mainapp/university_list.html'
    return render(request, template_name, context)


def university(request):
    if request.method == 'GET':
        form = UniversityForm()
        template_name = 'mainapp/university.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('university_list')
        else:
            template_name = 'mainapp/university.html'
            context = {'form': form}
            return render(request, template_name, context)


def university_delete(request, pk):
    university = University.objects.get(pk=pk)
    university.delete()
    return redirect('university_list')


def university_edit(request, pk):
    university = University.objects.get(pk=pk)
    if request.method == 'GET':
        form = UniversityForm(instance=university)
        template_name = 'mainapp/university.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = UniversityForm(request.POST, instance=university)
        if form.is_valid():
            form.save()
            return redirect('university_list')
        else:
            template_name = 'mainapp/university.html'
            context = {'form': form}
            return render(request, template_name, context)


def university_detail(request, pk):
    university = University.objects.get(pk=pk)
    context = {'university': university}
    template_name = 'mainapp/university_detail.html'
    return render(request, template_name, context)


# ================= STUDENT VIEWS =================

def student_list(request):
    students = Student.objects.all().order_by('first_name')
    context = {'students': students}
    template_name = 'mainapp/student_list.html'
    return render(request, template_name, context)


def student(request):
    if request.method == 'GET':
        form = StudentForm()
        template_name = 'mainapp/student.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            template_name = 'mainapp/student.html'
            context = {'form': form}
            return render(request, template_name, context)


def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('student_list')


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        form = StudentForm(instance=student)
        template_name = 'mainapp/student.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            template_name = 'mainapp/student.html'
            context = {'form': form}
            return render(request, template_name, context)


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    context = {'student': student}
    template_name = 'mainapp/student_detail.html'
    return render(request, template_name, context)
