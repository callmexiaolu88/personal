#!/usr/bin/env python

import datetime
from django.http import HttpResponse,HttpResponseNotFound

def index(request):
    dt=datetime.datetime.now()
    html="<h>Current data time is :{0}</h>".format(dt)
    html=html+"<a href='/first/detail/3/4'> 计算3+4</a>"
    return HttpResponse(html)


def detail(request,p1,p2):
    return HttpResponse("<b>{0}+{1}={3}</b>".format(p1,p2,p1+p2))