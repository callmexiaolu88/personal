#!/usr/bin/env python

from django.urls import path
from firstbag import pages

urlpatterns=[
    path("",pages.index),
    path("detail/",pages.detail),
]