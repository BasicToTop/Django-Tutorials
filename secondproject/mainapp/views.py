from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.


def home(request):
    trainer_name = "Ram S. from basic to top"
    # return HttpResponse("Welcome to the Main App Home Page")
    template_name = 'mainapp/home.html'
    context = {"trainer": trainer_name}  # key and value pairs
    return render(request, template_name, context)


def about(request):
    template_name = 'mainapp/about.html'
    context = {}
    return render(request, template_name, context)


def table_view(request):
    template_name = 'mainapp/table.html'
    context = {}
    return render(request, template_name, context)


def form_view(request):
    print('request.method ', request.method)
    if request.method == "GET":
        print(request.method)
        template_name = 'mainapp/form.html'
        context = {}
        return render(request, template_name, context)
    if request.method == 'POST':
        print(request.method)
        print('Custer send the data:--')
        # data = request.POST
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        phoneno = request.POST.get('phoneno')
        customer_data = {
            "fullname":fullname,
            "email":email,
            "dob":dob,
            "phoneno":phoneno,
        }
        print("DATA : ",customer_data)
        return redirect('form')
