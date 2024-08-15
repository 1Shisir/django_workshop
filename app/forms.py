from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'name':'Full Name',
            'age':'Age',
            'roll':'Roll No.',
            'phone':'Phone No.',
            'city':'City',
            'marks':'Marks',
            'faculty':'Faculty',
            'programme':'Programme',
        }