#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import sys
# import json
# from django.http import JsonResponse
# from book.models import book

from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from myCalendar.models import MyCalendar
import datetime

def index(request):
    context	= {}
    return render(request, 'myCalendar/month.html', context)

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def getdata(request):
    # print("list: " , "sssssssss")
    tasks = MyCalendar.objects.all()
    # response2 = MyCalendar.objects.filter(id=1)
    # response3 = MyCalendar.objects.get(id=1)

    response_data = []
    for task in tasks:
        one_data = {}
        one_data['id'] = task.id
        one_data['projectid'] = task.projectid
        one_data['task'] = task.task
        one_data['endtime'] = task.endtime
        response_data.append(one_data)


    # print("list: " , type(response_data), response_data)
    return JsonResponse(response_data,  safe=False)

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
