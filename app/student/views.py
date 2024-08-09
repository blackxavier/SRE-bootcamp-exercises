from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from student.models import Student
from student.serializers import (
    StudentListSerializer,
    StudentPostSerializer,
    StudentDetailSerializer,
)
from student.pagination import StudentPagination


class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all().order_by("date_created")
    serializer_class = StudentListSerializer
    pagination_class = StudentPagination

    @extend_schema(operation_id="list_students")
    def get(self, request):
        paginated_students = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(
            paginated_students, many=True, context={"request": request}
        )
        paginated_response = self.get_paginated_response(serializer.data)
        message = {
            "status": "success",
            "data": paginated_response.data,
        }
        return Response(message, status=status.HTTP_200_OK)

    @extend_schema(operation_id="create_students")
    def post(self, request):
        serializer = StudentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"status": "success", "data": serializer.data}
            return Response(message, status=status.HTTP_201_CREATED)
        message = {"status": "failed", "data": serializer.errors}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    serializer_class = StudentDetailSerializer

    def get(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = self.serializer_class(student)
            message = {"status": "success", "data": serializer.data}
            return Response(message, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            message = {"status": "failed", "data": "Student not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, pk):
        serializer_class = StudentPostSerializer
        try:
            student = Student.objects.get(pk=pk)
            serializer = serializer_class(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {"status": "success", "data": serializer.data}
                return Response(message, status=status.HTTP_200_OK)
            message = {"status": "failed", "data": serializer.errors}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            message = {"status": "failed", "data": "Student not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            message = {"status": "success", "data": "Student deleted"}
            return Response(message, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            message = {"status": "failed", "data": "Student not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def healthcheck(request: Request):
    message = {"status": "success", "message": "Server is healthy"}
    return Response(message, status=status.HTTP_200_OK)
