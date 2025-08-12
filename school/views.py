from django.shortcuts import render, redirect
from .models import Teacher, Student, Grade
from .forms import CreateTeacherForm, CreateStudentForm, CreateGradeForm


def home(request):
    return render(request, 'school/home.html')


def teacher(request, id):
    t = Teacher.objects.get(id=id)
    return render(request, 'school/teacher.html', {'t': t})


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teachers_list.html', {'teachers': teachers})


def delete_teacher(request, id):
    Teacher.objects.get(id=id).delete()
    return redirect('teachers_list')


def create_teacher(request):
    if request.method == "POST":
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            n = request.POST['name']
            s = request.POST['subject']
            Teacher.objects.create(name=n, subject=s)
            return redirect('teachers_list')

    elif request.method == "GET":
        form = CreateTeacherForm()
        return render(request, 'school/create_teacher.html', {'form': form})


def student(request, id):
    s = Student.objects.get(id=id)
    return render(request, 'school/student.html', {'s': s})


def students_list(request):
    students = Student.objects.all()
    return render(request, 'school/students_list.html', {'students': students})


def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('students_list')


def create_student(request):
    if request.method == "POST":
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            n = request.POST['name']
            f = request.POST['family']
            a = request.POST['age']
            t_id = request.POST['teacher']
            
            t_obj = Teacher.objects.get(id=t_id)
            
            Student.objects.create(name=n, family=f, age=a, teacher=t_obj)
            return redirect('students_list')
        
    form = CreateStudentForm()
    return render(request, 'school/create_student.html', {'form': form})


def grade(request, id):
    g = Grade.objects.get(id=id)
    return render(request, 'school/grade.html', {'g': g})


def grades_list(request):
    grades = Grade.objects.all()
    return render(request, 'school/grades_list.html', {'grades': grades})


def delete_grade(request, id):
    Grade.objects.get(id=id).delete()
    return redirect('grades_list')


def create_grade(request):
    if request.method == "POST":
        form = CreateGradeForm(request.POST)
        if form.is_valid():
            std_id = request.POST['student']
            std_obj = Student.objects.get(id=std_id)
            
            scr = request.POST['score']
            
            Grade.objects.create(student=std_obj, score=scr)
            return redirect('grades_list')

    elif request.method == "GET":
        form = CreateGradeForm()
        return render(request, 'school/create_grade.html', {'form': form})


