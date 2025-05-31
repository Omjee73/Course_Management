from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list_create, name='course-list-create'),
    path('students/', views.student_list_create, name='student-list-create'),
    path('courses/form/', views.course_create_form, name='course-create-form'),
    path('students/form/', views.student_create_form, name='student-create-form'),
]
