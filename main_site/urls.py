#!/usr/bin/python
# -*- coding: utf-8 -*-
"""forum URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^wellness/$', views.wellness, name='wellness'),
    url(r'^business/$', views.business, name='business'),
    url(r'^message_call/$', views.message_call, name='message_call'),
    url(r'^business/(?P<pk>[0-9]+)/$', views.bullet_detail, name='bullet_detail'),
    url(r'^forsome/(?P<slug>[-\w]+)/$', views.category, name='category'),
	url(r'^products/(?P<pk>[0-9]+)/$', views.category_description, name='category_description'),
	url(r'^stocks/(?P<pk>[0-9]+)/$', views.stock_detail, name='stock_detail'),
	url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^videos/$', views.video_gallery, name='video_gallery'),
	url(r'^form_call/$', views.form_call, name='form_call'),
]
