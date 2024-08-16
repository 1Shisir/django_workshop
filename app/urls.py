from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contacts/',views.contacts, name='contacts'),
    path('read/',views.read, name='read'),
    path('success/',views.success, name='success'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('delete/<int:id>/',views.remove, name='remove'),
    path('student/',views.student, name='student'),
    path('create/',views.create, name='create'),
    path('update/<int:id>/',views.update, name= 'update'),
    path('login/',views.loginn, name = 'login'),
    path('logout/', views.logoutt,name= 'lohout'),
    path('register/', views.registerr, name= 'register'),
    path('courses/', views.courses, name= 'courses'),
    path('reports/', views.reports, name= 'reports'),
    path('settings/', views.settings, name= 'settings'),

]