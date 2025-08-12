from django.contrib import admin
from .models import Teacher, Student, Grade


admin.site.register([Teacher, Student, Grade])
# admin.site.register(Student)
