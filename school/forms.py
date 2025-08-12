from django import forms
from .models import Teacher, Student
from django.core.validators import MinValueValidator, MaxValueValidator

class CreateTeacherForm(forms.Form):
    name = forms.CharField(label='name:')
    subject = forms.CharField(label='subject:')
    

class CreateStudentForm(forms.Form):
    name = forms.CharField(label='name:')
    family = forms.CharField(label='family:')
    age = forms.IntegerField(label='age:')
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    

class CreateGradeForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    score = forms.DecimalField(label='score:')