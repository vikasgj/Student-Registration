from django.urls import path
from .views import register_student, student_list, student_details

urlpatterns = [
    path('',register_student, name = 'register_student'),
    path('students/', student_list, name = 'student_list'),
    path('students/<int:student_id>/', student_details, name = 'student_details')
]