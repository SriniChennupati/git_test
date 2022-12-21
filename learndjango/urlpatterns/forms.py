#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 23:35:22 2022

@author: srinivas
"""

from django import forms

class urlform(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='your email')
    text = forms.CharField(widget=forms.Textarea)