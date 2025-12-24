from django.shortcuts import render, redirect
from testapp.forms import StudentForm
from testapp.models import Student
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

            obj = Student(name=student_name, rollno=student_rollno,
                          father_name=student_father_name, mother_name=student_mother_name,
                          gender=student_gender, email=student_email)
            obj.save()

            return redirect('student_list')

            # template_name = 'student_create.html'
            # context = {'form': form, 'student_name': student_name, 'student_rollno': student_rollno, 'student_father_name': student_father_name,
            #            'student_mother_name': student_mother_name, 'student_gender': student_gender, 'student_email': student_email}

            # return render(request, template_name, context)
        else:
            print('Form Errors:- ', form.errors)

        # form = StudentForm(request.POST)


def student_list(request):
    if request.method == 'GET':
        print('student list')
        records = Student.objects.all()
        print('records:', records)
        # for data in records:
        #     print("Student Name:", data.name)
        #     print("Student RollNo:", data.rollno)
        #     print("Student Father Name:", data.father_name)
        #     print("Student Mother Name:", data.mother_name)
        #     print("Student  Gender:", data.gender)
        #     print("Student Email:", data.email)
        #     print('*'*30)

        template_name = 'student_list.html'
        context = {'records': records}
        return render(request, template_name, context)


def student_delete(request, record_id):
    if request.method == 'GET':
        print('#'*30)
        print('Reqeust for delete student record id:', record_id)

        # is it responbile to fetch record based on id
        record = Student.objects.get(id=record_id)
        print('Record to be deleted:', record.name)
        print('*'*30)
        record.delete()  # deleting the record
        return redirect('student_list')
