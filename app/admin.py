from django.contrib import admin
from .models import Student, Teacher, Course

admin.site.register([Student, Teacher, Course])
