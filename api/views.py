from django.http import JsonResponse
from django.shortcuts import render
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])
def studentView(request):
    if request.method == 'GET':
        student = Student.objects.filter(age=16)
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)