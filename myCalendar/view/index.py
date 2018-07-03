#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import sys
# import json
# from django.http import JsonResponse
# from book.models import book

from django.shortcuts import render
import json
from django.http import HttpResponse
from myCalendar.models import MyCalendar

def index(request):
    context	= {}
    return render(request, 'myCalendar/month.html', context)

def getdata(request):
    # print("list: " , "sssssssss")
    list = MyCalendar.objects.all()
    # response2 = MyCalendar.objects.filter(id=1)
    # response3 = MyCalendar.objects.get(id=1)
    response_data = []
    one_data = {}
    one_data['id'] = list[0].id
    one_data['projectid'] = list[0].projectid
    one_data['task'] = list[0].task
    one_data['endtime'] = list[0].endtime

    response_data.append(one_data)

    # print("list: " , type(response_data), response_data)
    return HttpResponse(json.dumps(response_data), content_type='application/json')

# def aboutUs(request):
#     context	= {}
#     return render(request, 'home/aboutUs.html', context)
#
#
# def getdata(request):
#     # context	= {}
#     # return render(request, 'home/index.html', context)
#     response_data = {}
#     response_data['result'] = 'failed'
#     # response_data['message'] = 'You messed up'
#     # return HttpResponse(json.dumps(response_data), content_type="application/json")
#     return HttpReponse(response_data, content_type='application/json')
