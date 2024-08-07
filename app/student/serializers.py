from rest_framework import serializers
from student.models import Student


class StudentListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        extra_kwargs = {"url": {"view_name": "student-detail", "lookup_field": "pk"}}
        fields = [
            "url",
            "id",
            "first_name",
            "last_name",
            "student_id",
            "email",
            "gender",
        ]


# class StudentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ("first_name", "last_name", "student_id", "email", "gender")


class StudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "gender",
            "phone_number",
            "date_of_birth",
        ]


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
