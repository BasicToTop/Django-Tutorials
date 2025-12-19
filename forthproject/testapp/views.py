from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.


def home_view(request):
    template_name = 'home.html'
    return render(request, template_name)


def student_create(request):
    if request.method == 'GET':
        print('Default Method:- ', request.method)
        form = StudentForm()

        template_name = 'student_create.html'
        context = {'form': form}
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = StudentForm(request.POST)  # bind form with POST data

        if form.is_valid():  # validation check
            student_name = form.cleaned_data['name']
            student_rollno = form.cleaned_data['rollno']
            student_father_name = form.cleaned_data['father_name']
            student_mother_name = form.cleaned_data['mother_name']
            student_gender = form.cleaned_data['gender']
            student_email = form.cleaned_data['email']
            print('Student Details Submitted Successfully!!!')
            print('Student Name:- ', student_name)
            print('Student RollNo:- ', student_rollno)
            print('Student Father Name:- ', student_father_name)
            print('Student Mother Name:- ', student_mother_name)
            print('Student Gender:- ', student_gender)
            print('Student Email:- ', student_email)

            template_name = 'student_create.html'
            context = {'form':form, 'student_name': student_name, 'student_rollno': student_rollno, 'student_father_name': student_father_name, 'student_mother_name': student_mother_name, 'student_gender': student_gender, 'student_email': student_email}

            return render(request, template_name, context)
        else:
            print('Form Errors:- ', form.errors)

        # form = StudentForm(request.POST)
