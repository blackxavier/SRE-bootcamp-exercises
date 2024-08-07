from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "student_id",
        "email",
    )
    search_fields = ("first_name", "last_name", "student_id", "email")
    list_filter = ("gender",)
    ordering = ("last_name", "first_name")


admin.site.register(Student, StudentAdmin)
