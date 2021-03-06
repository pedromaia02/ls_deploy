# 2017.09.22 10:08:01 BRT
#Embedded file name: /home/pedro/ls_deploy/ls_deploy/inss/src/inssonline/urls.py
"""inssonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from fortalposts import views
from natalposts import views
from imperatrizposts import views
from accounts.views import login_view, register_view, logout_view

urlpatterns = [url('^admin/', admin.site.urls),
 url('^inssfortaleza/', include('fortalposts.urls', namespace='fortalposts')),
 url('^inssnatal/', include('natalposts.urls', namespace='natalposts')),
 url('^inssimperatriz/', include('imperatrizposts.urls', namespace='imperatrizposts')),
 url('^inssmossoro/', include('mossoroposts.urls', namespace='mossoroposts')),
 url('^login/', login_view, name='login'),
 url('^logout/', logout_view, name='logout')]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
