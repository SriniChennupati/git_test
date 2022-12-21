"""from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.
def urlpatterns(request,id=3):
    
    id_number = id
    query = request.GET.get('test','')
    ip = request.META['REMOTE_ADDR']
    values_for_templates={'id': id_number, 'ip_address':ip}
    return render(request, 'urlpatterns/id.html', values_for_templates)

    return HttpResponsePermanentRedirect(reverse('homepage'))"""

from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import loader, Context
from django.urls import reverse
from django.shortcuts import render
from .forms import urlform

def urlpatterns(request, id=3):
    
    id_number = id
    query = request.GET.get('test','')
    ip = request.META['REMOTE_ADDR']
    values_for_templates={'id': id_number, 'ip_address':ip}
    
    if request.method == 'POST':
    #output = t.render(values_for_templates)
    #c = Context(values_for_templates)
        response=HttpResponse(content_type='text/html')
        t = loader.get_template('urlpatterns/id.html')
        return response(t.render(values_for_templates))
    #return HttpResponsePermanentRedirect(reverse('homepage'))
    form = urlform()
    return render(request, 'urlpatterns/inputform.html', {'form':form})
    