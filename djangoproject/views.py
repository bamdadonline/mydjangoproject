from django.shortcuts import HttpResponse
from django.shortcuts import render

def about(request):
    # return HttpResponse("About Page")
    return render(request, 'about.htm')

def home(request):
    # return HttpResponse("Home Page")
    return render(request, 'home.htm')