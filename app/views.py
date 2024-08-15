from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView




# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('About Page')

def contacts(request):
    return HttpResponse('Contact Us Page')    

def read(request):
    students = Student.objects.all()
    return render(request, 'read.html', {'students':students})

def success(request):
    return render(request, 'success.html')  

@login_required
def dashboard(request):
    students = Student.objects.all()
    return render(request, 'dashboard.html', {'students':students})

@login_required
def remove(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student')   

@login_required
def create(request):
    form = StudentForm()
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        roll = request.POST['roll']
        phone = request.POST['phone']
        city = request.POST['city']
        marks = request.POST['marks']
        faculty = request.POST['faculty']
        programme = request.POST['programme']
        student = Student(name=name, age=age, roll=roll, phone=phone, city=city, marks=marks, faculty=faculty, programme=programme)
        student.save()
        return redirect('student')
    return render(request, 'create.html', {'form':form})    

def student(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'student.html', {'students':students})  


@login_required
def update(request,id):
    student = Student.objects.get(id = id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    return render(request, 'update.html',{'form':form,'students':student}) 


def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    return render(request, 'login.html')

@login_required
def logoutt(request):
    logout(request)
    return redirect('login')    


 
    
