from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Student(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)
    age = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.family} ({self.age}) - Teacher: {self.teacher.name} ({self.teacher.subject})"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=4, decimal_places=2, validators=[
                                MinValueValidator(0), MaxValueValidator(20)])

    def __str__(self):
        return f"{self.student.name} - {self.student.teacher.subject}: {self.score}"
