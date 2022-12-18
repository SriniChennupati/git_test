#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:18:56 2022

@author: srinivas
"""

from django.shortcuts import render

def page_not_found(request):
    return(render, '404.html')