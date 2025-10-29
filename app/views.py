from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Teacher, Course
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer

class StudentAllApiViev(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many = True)

        return Response(serializer.data)
    
class CreateStudentApiViev(APIView):
    def post(self, request):
        name = request.data
        print(name)
        return Response(name)


class StudentApiViev(APIView):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)

        return Response(serializer.data)
    
class TeacherAllApiViev(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many = True)

        return Response(serializer.data)

class TeacherApiViev(APIView):
    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher)

        return Response(serializer.data)
    
class CourseAllApiViev(APIView):
    def get(self, request):
        student = Course.objects.all()
        serializer = CourseSerializer(student, many = True)

        return Response(serializer.data)
    
class CourseApiViev(APIView):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)

        return Response(serializer.data)




