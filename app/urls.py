
from django.urls import path
from .views import GetStudentAllApiViev, GetTeacherAllApiViev, GetCourseAllApiViev, GetStudentApiViev
from .views import GetTeacherApiViev, GetCourseApiViev
urlpatterns = [
  path('all_student/', GetStudentAllApiViev.as_view()),
  path('all_teacher/', GetTeacherAllApiViev.as_view()),
  path('all_course/', GetCourseAllApiViev.as_view()),

  path('get_student/<int:pk>/', GetStudentApiViev.as_view()),
  path('get_teacher/<int:pk>/', GetTeacherApiViev.as_view()),
  path('get_course/<int:pk>/', GetCourseApiViev.as_view()),

]