from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_api, name='students'),  # for GET and POST of student taable
    path('students/<int:id>/', views.students_api, name='student_detail'),  # for GET, PUT, DELETE of student table individual elements 
    path('students_pno/', views.students_pno_api, name='students_pno'),  # for GET and POST of studentPno table 
    path('students_pno/<int:pno_id>/', views.students_pno_api, name='students_pno_detail'),  # for PUT and DELETE  of studentPno table 
]
