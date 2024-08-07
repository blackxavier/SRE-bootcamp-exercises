from rest_framework.views import APIView
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


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentListSerializer(
            students,
            many=True,
            context={
                "request": request,
            },
        )
        message = {
            "status": "success",
            "data": serializer.data,
        }
        return Response(message, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = StudentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"status": "success", "data": serializer.data}
            return Response(message, status=status.HTTP_201_CREATED)
        message = {"status": "failed", "data": serializer.errors}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentDetailSerializer(student)
            message = {"status": "success", "data": serializer.data}
            return Response(message, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            message = {"status": "failed", "data": "Student not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentPostSerializer(student, data=request.data)
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
