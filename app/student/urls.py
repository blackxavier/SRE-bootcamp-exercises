from django.urls import path
from django.urls import include
from django.contrib import admin
from student.views import StudentListCreateView, StudentDetailView, healthcheck

urlpatterns = [
    path("students/", StudentListCreateView.as_view(), name="student-list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("healthcheck/", healthcheck, name="healthcheck"),
]
