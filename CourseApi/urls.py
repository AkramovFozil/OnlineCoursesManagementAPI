from . import views
from django.urls import path

urlpatterns = [
    path('instructors/', views.InstructorList.as_view()),
    path('courses/', views.CourseList.as_view()),
    path('lessons/', views.LessonList.as_view()),
]
