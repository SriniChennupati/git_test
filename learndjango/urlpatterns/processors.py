#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:19:41 2022

@author: srinivas
"""

def url_values(request):
    path1 = request.path
    print(path1)
    return {'urlpath': path1}