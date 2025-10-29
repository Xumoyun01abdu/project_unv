
from django.urls import path
from .views import StudentAllApiViev, TeacherAllApiViev, CourseAllApiViev, StudentApiViev
from .views import TeacherApiViev, CourseApiViev, CreateStudentApiViev
urlpatterns = [
  path('all_student/', StudentAllApiViev.as_view()),
  path('all_teacher/', TeacherAllApiViev.as_view()),
  path('all_course/', CourseAllApiViev.as_view()),

  path('get_student/<int:pk>/', StudentApiViev.as_view()),
  path('get_teacher/<int:pk>/', TeacherApiViev.as_view()),
  path('get_course/<int:pk>/', CourseApiViev.as_view()),

  path('add_student/', CreateStudentApiViev.as_view())

]