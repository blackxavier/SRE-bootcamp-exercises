from django.db import models
import random


class Student(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10, choices=[("Male", "Male"), ("Female", "Female")]
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    student_id = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.student_id:
            self.student_id = self.generate_unique_student_id()
        super().save(*args, **kwargs)

    def generate_unique_student_id(self):
        while True:
            code = "".join(random.choices("0123456789", k=10))
            if not Student.objects.filter(student_id=code).exists():
                return code

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
