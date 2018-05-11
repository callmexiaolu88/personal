#!/usr/bin/env python

import datetime
from django.http import HttpResponse,HttpResponseNotFound

def index(request):
    dt=datetime.datetime.now()
    html="<h>Current data time is :{0}</h>".format(dt)
    return HttpResponse(html)