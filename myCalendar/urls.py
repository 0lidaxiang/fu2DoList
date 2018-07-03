#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from home.view.index import  *
from django.views.generic import TemplateView

urlpatterns = [
    # url('^index/$', index),
    url('^aboutUs/$', aboutUs),
    url('^index/$', TemplateView.as_view(template_name="myCalendar/month.html")),

]
