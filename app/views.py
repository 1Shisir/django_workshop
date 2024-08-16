from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User



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
    return render(request, 'dashboard.html', {'students':students, 'user':request.user})

@login_required
def remove(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student')   

@login_required(login_url='login')
def create(request):
    form = StudentForm()
    if request.method == 'POST':
        # user = request.user
        # name = request.POST['name']
        # age = request.POST['age']
        # roll = request.POST['roll']
        # phone = request.POST['phone']
        # city = request.POST['city']
        # marks = request.POST['marks']
        # faculty = request.POST['faculty']
        # programme = request.POST['programme']
        # student = Student(name=name, age=age, roll=roll, phone=phone, city=city, marks=marks, faculty=faculty, programme=programme)
        # student.save()
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)   
            student.user = request.user
            student.save()
            return redirect('student')
    return render(request, 'create.html', {'form':form})    

def student(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'student.html', {'students':students})  


@login_required(login_url='login')
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

@login_required(login_url='login')
def logoutt(request):
    logout(request)
    return redirect('login')  

def registerr(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password == re_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
        else:
            return HttpResponse('Password does not match')
    return render(request, 'register.html')

def courses(request):
    return render(request, 'courses.html')      

def reports(request):
    return render(request, 'reports.html')

def settings(request):
    return render(request, 'settings.html', {'user':request.user})
 
    
