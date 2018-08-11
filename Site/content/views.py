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

##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Legal Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##


def affiliate_marketing_disclosure(request):

    """ Load and render the affiliate_marketing_disclosure template """

    title = 'Disclosure - ArtsyVisions.com';
    template = 'content/legal/affiliate_marketing_disclosure.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def privacy_policy(request):

    """ Load and render the privacy_policy template """

    title = 'Privacy Policy - ArtsyVisions.com';
    template = 'content/legal/privacy_policy.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def questionnaire_disclaimer(request):

    """ Load and render the questionnaire_disclaimer template """

    title = 'Disclaimer - ArtsyVisions.com';
    template = 'content/legal/questionnaire_disclaimer.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def terms_of_service(request):

    """ Load and render the terms_of_service template """

    title = 'Terms of Service - ArtsyVisions.com';
    template = 'content/legal/terms_of_service.html'
    context = {
        'title': title,
    }
    return render(request, template, context)
