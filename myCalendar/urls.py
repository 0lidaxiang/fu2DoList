#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from myCalendar.view.index import  *
from django.views.generic import TemplateView

urlpatterns = [
    url('^getdata/$', getdata),
    # url('^aboutUs/$', aboutUs),
    url('^index/$', TemplateView.as_view(template_name="myCalendar/month.html")),

]
