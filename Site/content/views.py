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

from .models import VisionsList

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
##   Views for Visions Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##


def visions_all(request):

    """ Load and render the visions/all template """

    visions_list_obj = VisionsList('all')  # Reads the json files, etc.
    title = 'All Visions - ArtsyVisions.com';
    template = 'content/visions/all.html'
    context = {
        'title': title,
        'visions_list_obj': visions_list_obj,
    }
    return render(request, template, context)


def visions_person(request):

    """ Load and render the visions/person template """

    visions_list_obj = VisionsList('person')  # Reads the json files, etc.
    title = 'Individuals - ArtsyVisions.com';
    template = 'content/visions/person.html'
    context = {
        'title': title,
        'visions_list_obj': visions_list_obj,
    }
    return render(request, template, context)


def visions_people(request):

    """ Load and render the visions/people template """

    visions_list_obj = VisionsList('people')  # Reads the json files, etc.
    title = 'Pairs - ArtsyVisions.com';
    template = 'content/visions/people.html'
    context = {
        'title': title,
        'visions_list_obj': visions_list_obj,
    }
    return render(request, template, context)


def visions_groups(request):

    """ Load and render the visions/groups template """

    visions_list_obj = VisionsList('groups')  # Reads the json files, etc.
    title = 'Groups - ArtsyVisions.com';
    template = 'content/visions/groups.html'
    context = {
        'title': title,
        'visions_list_obj': visions_list_obj,
    }
    return render(request, template, context)


def visions_story(request, vision_file_no_ext=''):

    """ Load and render the visions/story template """

    visions_story_obj = {}
    visions_story_obj['vision_file_no_ext'] = vision_file_no_ext
    title = 'Story - ArtsyVisions.com';
    template = 'content/visions/story.html'
    context = {
        'title': title,
        'visions_story_obj': visions_story_obj,
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
