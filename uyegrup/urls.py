# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


@login_required(login_url='/giris/')
def ilksayfa(request):

    print "anasayfa"
    return render(request, 'index.html')


@csrf_protect
def cikis(request):
    logout(request)
    print "cikis, anasayfaya yönlendir"

    return redirect("/")


@csrf_protect
def giris(request):
    logout(request)
    mail = parola = ''
    if request.POST:
        mail = request.POST['mail']
        parola = request.POST['parola']

        print "giris, anasayfaya yönlendir, ", mail, parola

        user = authenticate(username=mail, password=parola)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'giris.html')


urlpatterns = [
    url(r'^$', ilksayfa),
    url(r'^giris/$', giris),
    url(r'^cikis/$', cikis),
    url(r'^admin/', admin.site.urls),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
