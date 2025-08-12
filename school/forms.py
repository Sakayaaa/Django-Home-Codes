from django import forms
from .models import Teacher, Student, Grade

# class CreateTeacherForm(forms.Form):
#     name = forms.CharField(label='name:')
#     subject = forms.CharField(label='subject:')

# class CreateStudentForm(forms.Form):
#     name = forms.CharField(label='name:')
#     family = forms.CharField(label='family:')
#     age = forms.IntegerField(label='age:')
#     teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())

# class CreateGradeForm(forms.Form):
#     student = forms.ModelChoiceField(queryset=Student.objects.all())
#     score = forms.DecimalField(label='score:')


class CreateTeacherForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = ['name', 'subject']

class UpdateTeacherForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = ['name', 'subject']


class CreateStudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ['name', 'family', 'age', 'teacher']

class CreateGradeForm(forms.ModelForm):
    class Meta():
        model = Grade
        fields = ['student', 'score']