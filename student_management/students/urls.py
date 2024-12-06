from django.urls import path
from . import views

urlpatterns = [
    # Students table routes
    path('students/', views.students_api, name='students'),  # for GET and POST of student table
    path('students/<int:id>/', views.students_api, name='student_detail'),  # for GET, PUT, DELETE of student table individual elements

    # StudentsPNo table routes
    path('students_pno/', views.students_pno_api, name='students_pno'),  # for GET and POST of studentPno table
    path('students_pno/<int:pno_id>/', views.students_pno_api, name='students_pno_detail'),  # for PUT and DELETE of studentPno table

    # Subject table routes
    path('subject/', views.subject_api, name='subject'),  # for GET and POST of subject table
    path('subject/<int:id>/', views.subject_api, name='subject_detail'),  # for GET, PUT, PATCH, DELETE of subject table

    # Scores table routes
    path('scores/', views.scores_api, name='scores'),  # for GET and POST of scores table
    path('scores/<int:id>/', views.scores_api, name='score_detail'),  # for GET, PUT, PATCH, DELETE of scores table
]
