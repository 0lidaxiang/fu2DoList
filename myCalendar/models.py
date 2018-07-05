# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class MyCalendar(models.Model):
    id = models.AutoField(primary_key=True)
    projectid = models.IntegerField()
    task = models.CharField(max_length=500)
    # ownerId = models.CharField(max_length=100)
    # add_time = models.DateTimeField(auto_now_add=True)
    endtime = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'mycalendar'
