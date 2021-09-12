from rest_framework.fields import JSONField
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .serializers import *
from .models import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def studentList(request):
    if request.method == 'GET':
        s = Student.objects.all()
        serializer = StudentSerializers(s,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def studentDetails(request,id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializers(student,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)
