from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

def about(request):
    return HttpResponse('About Page')

def contacts(request):
    return HttpResponse('Contact Us Page')    

def read(request):
    students = Student.objects.all()
    return render(request, 'read.html', {'students':students})
