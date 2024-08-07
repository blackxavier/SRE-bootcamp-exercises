import datetime
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from student.models import Student
from model_bakery import baker


class StudentTestCase(APITestCase):
    # create setup method
    def setUp(self):
        self.client = APIClient()
        self.student = baker.make(Student)

    def test_student_model(self):
        self.assertTrue(isinstance(self.student, Student))

    def test_string_representation(self):
        # test string representation
        self.assertEqual(
            str(self.student),
            f"{self.student.first_name} {self.student.last_name} ({self.student.student_id})",
        )

    def test_healthcheck(self):
        url = reverse("healthcheck")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unique_id_is_enforced(self):
        # tests the uniqueness of each instance ID
        with self.assertRaises(IntegrityError):
            baker.make(Student, student_id=self.student.student_id)

    def test_date_created(self):
        # tests the date created field
        self.assertIsInstance(self.student.date_created, datetime.datetime)

    def test_date_modified(self):
        # tests the date created field
        self.assertIsInstance(self.student.date_modified, datetime.datetime)

    def test_get_students(self):
        # test retrieving all student data
        url = reverse("student-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        # test creating student data
        url = reverse("student-list")
        data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "date_of_birth": "2001-02-02",
            "gender": "Female",
            "email": "jane.smith@example.com",
            "phone_number": "+987654321",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_student_detail(self):
        # test retrieving singular student data by ID
        url = reverse("student-detail", kwargs={"pk": self.student.pk})
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]["first_name"], self.student.first_name)

    def test_full_update_student(self):
        # test updating student data (full update)
        url = reverse("student-detail", kwargs={"pk": self.student.pk})
        data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "date_of_birth": "2001-02-02",
            "gender": "Female",
            "email": "jane.smith@example.com",
            "phone_number": "+987654321",
        }
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_student(self):
        # test updating student data (pattial update)
        url = reverse("student-detail", kwargs={"pk": self.student.pk})
        data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "date_of_birth": "2001-02-02",
            "gender": "Female",
        }
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student(self):
        # test deleting student data
        url = reverse("student-detail", kwargs={"pk": self.student.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
