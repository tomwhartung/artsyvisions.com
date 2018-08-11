""" views.py for our content app

Purpose: define the views for this app
Author: Tom W. Hartung
Date: Summer, 2018.
Copyright: (c) 2018 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import View


def home(request):

    """ Load and render the Home page template """

    title = 'Home - ArtsyVisions.com';
    template = 'content/home.html'
    context = {
        'title': title,
    }
    return render(request, template, context)
