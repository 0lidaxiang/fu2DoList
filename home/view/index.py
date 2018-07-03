#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import sys
# import json
# from django.http import JsonResponse
# from book.models import book

from django.shortcuts import render
import json
from django.http import HttpResponse

def index(request):
    context	= {}
    return render(request, 'home/index.html', context)

def aboutUs(request):
    context	= {}
    return render(request, 'home/aboutUs.html', context)


def getdata(request):
    # context	= {}
    # return render(request, 'home/index.html', context)
    response_data = {}
    response_data['result'] = 'failed'
    # response_data['message'] = 'You messed up'
    # return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpReponse(response_data, content_type='application/json')
