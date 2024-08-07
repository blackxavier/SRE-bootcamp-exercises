from django.urls import path
from django.urls import include
from django.contrib import admin
from student.views import StudentListView, StudentDetailView, healthcheck

urlpatterns = [
    path("", StudentListView.as_view(), name="student-list"),
    path("<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("healthcheck/", healthcheck, name="healthcheck"),
]
