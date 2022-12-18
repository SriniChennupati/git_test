"""learndjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView


from learndjango.contactus import views  
from learndjango.urlpatterns import views as up
ur_patterns = [
    re_path(r'', up.urlpatterns),
    re_path(r'^urlpatters/(\d+)/', up.urlpatterns)
        ]
#handler404 = 'learndjango.utils.views.page_not_found'
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name='homepage.html'), name="homepage"),
    path(r'about/', views.contactus, name='about'),
    path(r'admin/', admin.site.urls),
    path(r'urlpatterns', include(ur_patterns))
    #path(r'urlpatterns/', up.urlpatterns),
    #re_path(r'urlpatterns/(\d+)/', up.urlpatterns)
    #path(r'urlpatterns/', include('learndjango.urlpatterns.urls'))
]
