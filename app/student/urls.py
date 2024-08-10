from django.urls import path
from student.views import StudentListCreateView, StudentDetailView, healthcheck

urlpatterns = [
    path("students/", StudentListCreateView.as_view(), name="student-list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("healthcheck/", healthcheck, name="healthcheck"),
]
