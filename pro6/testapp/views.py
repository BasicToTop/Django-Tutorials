from django.shortcuts import render, redirect
from testapp.forms import ContactUsForm
from testapp.models import ContactUs
# Create your views here.


def home(request):
    template_name = 'testapp/home.html'
    context = {}
    return render(request, template_name, context)


def contact(request):
    if request.method == 'GET':
        form = ContactUsForm()
        template_name = 'testapp/contact.html'
        context = {
            "page_name": "Contact Us",
            'form': form
        }
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            obj = ContactUs(
                name=name,
                email=email,
                phone_number=phone_number,
                gender=gender
            )
            obj.save()
            return redirect('home')
        template_name = 'testapp/contact.html'
        context = {
            "page_name": "Contact Us",
            'form': form
        }
        return render(request, template_name, context)
