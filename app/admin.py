from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Student, Teacher, Course

@admin.register(Student)
class CustomAdminClass(ModelAdmin):
    list_display = ['name', 'age', 'address']

@admin.register(Teacher)
class CustomAdminClass(ModelAdmin):
    list_display = ['name', 'age', 'course']

@admin.register(Course)
class CustomAdminClass(ModelAdmin):
    list_display = ['name', 'price', 'student']
