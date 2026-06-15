from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student(request):
    classes = [ {
        "name": "John Doe",
        "age": 20,
        "major": "Computer Science"
    }]
    return HttpResponse(classes)