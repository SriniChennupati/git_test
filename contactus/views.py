from django.shortcuts import render

# Create your views here.

def contactus(request):
    
    return render(request,'about/contactus.html')
