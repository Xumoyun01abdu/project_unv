from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=220)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=110)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


