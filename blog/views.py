from django.shortcuts import render


def home(request):
    return render(request=request, template_name='blog/home.html')


def inscription(request):
    return render(request=request, template_name='blog/inscription.html')


def hello(request):
    return render(request=request, template_name='blog/hello.html')
