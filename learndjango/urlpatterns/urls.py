#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:46:20 2022

@author: srinivas
"""

from django.urls import re_path
from . import views

urlpatterns = [
        re_path(r'', views.urlpatterns),
        re_path(r'urlpatterns/(\d+)/', views.urlpatterns)
    ]