from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, HttpResponse

from .models import Student
from django.http import JsonResponse

from django.core.serializers import serialize

# Create your views here.


def home(request):
    return HttpResponse('<h1>API Page</h1>')


def manual_api(request):
    data = {
        "first_name": 'Barry',
        'last_name': 'Mitchell',
        'number': 5000
    }
    return JsonResponse(data)


def student_list_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_count = Student.objects.count()
        student_list = []
        for student in students:
            student_list.append({
                'first_name': student.first_name,
                'last_name': student.last_name,
                'number': student.number
            })
        data = {
            'students': student_list,
            'student_count': student_count
        }
        return JsonResponse(data)


def student_list_api2(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_count = Student.objects.count()
        student_data = serialize("python", students)

        data = {
            'students': student_data,
            'student_count': student_count
        }
        return JsonResponse(data)


@csrf_exempt
def student_add_api(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        student_data = {}
        student_data['first_name'] = post_body.get('first_name')
        student_data['last_name'] = post_body.get('last_name')
        student_data['number'] = post_body.get('number')
        # validation required
        student = Student.objects.create(**student_data)
        data = {
            'message': f"Student {student.last_name} added successfully"
        }
        return JsonResponse(data, status=201)


@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        # print(type(serializer))
        # print(type(serializer.data))
        # print(serializer)
        # print('----------------------------')
        # print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message': f"Student {serializer.validated_data.get('last_name')} added successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
