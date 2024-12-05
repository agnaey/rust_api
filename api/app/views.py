from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics,mixins

# Create your views here.


def fun1(req):
    d={'name':'agnaey','age':21}
    return JsonResponse(d)

def fun2(req):
    if req.method=='GET':
        d=Project_user.objects.all()
        s=Sample(d,many=True)
        return JsonResponse(s.data,safe=False)
    
@csrf_exempt
def fun3(req):
    if req.method=='GET':
        d=Project_user.objects.all()
        s=Model_serializer(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        s=Model_serializer(data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)