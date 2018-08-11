""" urls.py for our content app

Purpose: define the urls for this app
Author: Tom W. Hartung
Date: Summer, 2018.
Copyright: (c) 2018 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
    https://docs.djangoproject.com/en/2.1/intro/tutorial01/#write-your-first-view
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),

]

