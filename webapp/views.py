from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import responses, Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializers
import datetime


def hello(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3><p>Dear Concern I am a regular viewer of this learning website. <br> But, I found a design issue that it show a horizontal overflow in all pages.<br> If it will remove then page looks more fantastic. Kind regards, Minhaz Uddin Emon http://minhazemon21.github.io/minhazemon/</p></body></html>" % now

    return HttpResponse(html)  # rendering the template in HttpResponse

class employeeList(APIView):
    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeesSerializers(employees1, many=True)
        return Response (serializer.data)

    def post(self):
        pass

