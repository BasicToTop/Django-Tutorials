from django.shortcuts import render
# Create your views here.


def test(request):
    template_name = 'testapp/test.html'
    context = {}
    return render(request, template_name, context)
