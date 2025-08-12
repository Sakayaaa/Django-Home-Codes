from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    
    path('teachers_list/', views.teachers_list, name='teachers_list'),
    path('teacher/<int:id>', views.teacher, name='teacher'),
    path('delete_teacher/<int:id>', views.delete_teacher, name='delete_teacher'),
    path('create_teacher/', views.create_teacher, name='create_teacher'),
    path('update_teacher/<int:pk>', views.update_teacher, name='update_teacher'),
    
    path('students_list/', views.students_list, name='students_list'),
    path('student/<int:id>', views.student, name='student'),
    path('delete_student/<int:id>', views.delete_student, name='delete_student'),
    path('create_student/', views.create_student, name='create_student'),
    path('update_student/<int:id>', views.update_student, name='update_student'),
    
    path('grades_list/', views.grades_list, name='grades_list'),
    path('grade/<int:id>', views.grade, name='grade'),
    path('delete_grade/<int:id>', views.delete_grade, name='delete_grade'),
    path('create_grade/', views.create_grade, name='create_grade'),
    path('update_grade/<int:id>', views.update_grade, name='update_grade'),
]
