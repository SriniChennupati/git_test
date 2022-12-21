#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 00:03:53 2022

@author: srinivas
"""

class middleware_urlpatterns():
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        
        response=self.get_response(request)
        return response
    