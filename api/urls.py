from django.urls import path
from .views import CourseListCreateView, StudentListCreateView, RegisterUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view()),
    path('students/', StudentListCreateView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
# This code defines the URL patterns for the API, including endpoints for courses, students, user registration, and JWT authentication.
# The `CourseListCreateView` and `StudentListCreateView` handle listing and creating courses and students, respectively.