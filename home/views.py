from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("about")


def contact(request):
    return HttpResponse("contact")

def state(request):
    return HttpResponse("state")


def central(request):
    return HttpResponse("cental")