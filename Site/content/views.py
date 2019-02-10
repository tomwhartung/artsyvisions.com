""" views.py for our content app

Purpose: define the views for this app
Author: Tom W. Hartung
Date: Summer, 2018.
Copyright: (c) 2018 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import View

from .affiliate_marketing import AffiliateLinks
from .models import VisionsList
from .models import VisionStory


def home(request):

    """ Load and render the Home page template """

    title = 'Home - ArtsyVisions.com';
    template = 'content/home.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def index(request):

    """ Load and render the Story page using the body and notes templates """

    visions_story_obj = VisionStory('index')
    visions_story_data = visions_story_obj.visions_story_data
    title = visions_story_data['vision_dict']['title'] + ' - ArtsyVisions.com'
    template = 'content/visions/story.html'
    context = {
        'title': title,
        'visions_story_data': visions_story_data,
    }
    return render(request, template, context)


def versions(request):

    """ Load and render the versions template """

    import platform
    python_version = platform.python_version()
    import django
    django_version_1 = django.VERSION
    django_version_2 = django.get_version()

    from .models import DJANGO_DEBUG
    from .models import RUNNING_LOCALLY

    template = loader.get_template('content/versions.html')
    context = {
        'django_version_1': django_version_1,
        'django_version_2': django_version_2,
        'python_version': python_version,
        'DJANGO_DEBUG': DJANGO_DEBUG,
        'RUNNING_LOCALLY': RUNNING_LOCALLY,
    }
    return HttpResponse(template.render(context, request))


##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Visions Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##


def visions_all(request):

    """ Get the data needed and load and render the visions/all template """

    visions_list_obj = VisionsList('all')  # Reads the json files, etc.
    title = 'All Visions - ArtsyVisions.com';
    template = 'content/visions/all.html'
    context = {
        'title': title,
        'visions_list_obj': visions_list_obj,
    }
    return render(request, template, context)


def visions_person(request):

    """ Get the data needed and load and render the visions/person template """

    visions_list_obj = VisionsList('person')  # Reads the json files, etc.
    title = 'Individuals - ArtsyVisions.com';
    template = 'content/visions/person.html'
    context = {
        'title': title,
        'visions_list_obj': visions_list_obj,
    }
    return render(request, template, context)


def visions_pairs(request):

    """ Get the data needed and load and render the visions/pairs template """

    visions_list_obj = VisionsList('pairs')  # Reads the json files, etc.
    title = 'Pairs - ArtsyVisions.com';
    template = 'content/visions/pairs.html'
    context = {
        'title': title,
        'visions_list_obj': visions_list_obj,
    }
    return render(request, template, context)


def visions_groups(request):

    """ Get the data needed and load and render the visions/groups template """

    visions_list_obj = VisionsList('groups')  # Reads the json files, etc.
    title = 'Groups - ArtsyVisions.com';
    template = 'content/visions/groups.html'
    context = {
        'title': title,
        'visions_list_obj': visions_list_obj,
    }
    return render(request, template, context)


def visions_story(request, vision_file_no_ext=''):

    """
    Get the data needed for the passed-in parameter, then
    Load and render the visions/story template
    """

    visions_story_obj = VisionStory(vision_file_no_ext)
    visions_story_data = visions_story_obj.visions_story_data
    title = visions_story_data['vision_dict']['title'] + ' - ArtsyVisions.com'

    afl_links = AffiliateLinks()
    afl_content = afl_links.afl_content
    afl_button = afl_links.afl_content

    template = 'content/visions/story.html'
    context = {
        'title': title,
        'visions_story_data': visions_story_data,
        'afl_content': afl_content,
        'afl_button': afl_button,
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


##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views to suppoert shortcuts e.g., to a specific gallery and 404 not found
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def process_shortcut(request, unknown_page='default_unk_pg_1'):

    """ Process recognized shortcuts, and default to 404 """

    redirect_dict = {
        'ah': '/visions/story/0060-person-alexander_hamilton',
        'alexander_hamilton': '/visions/story/0060-person-alexander_hamilton',
        'er': '/tbd',
        'eleanor_roosevelt': '/tbd',
        'fdr': '/tbd',
        'franklin_roosevelt': '/tbd',
        'st': '/visions/story/0020-pairs-star_trek-spock_and_mccoy',
        'star_trek': '/visions/story/0020-pairs-star_trek-spock_and_mccoy',
        'sw': '/0070-pairs-star_wars-leia_and_han',
        'tj': '/visions/story/0040-person-thomas_jefferson',
        'thomas_jefferson': '/visions/story/0040-person-thomas_jefferson',
        'tr': '/visions/story/0060-person-theodore_roosevelt',
        'theodore_roosevelt': '/visions/story/0060-person-theodore_roosevelt',
        'xf': '/visions/story/0050-pairs-x_files-mulder_and_scully',
        'x-files': '/visions/story/0050-pairs-x_files-mulder_and_scully',
        'x_files': '/visions/story/0050-pairs-x_files-mulder_and_scully',
    }

    unk_pg_lc = unknown_page.lower()

    if unk_pg_lc in redirect_dict.keys():
        redirect_url = redirect_dict[unk_pg_lc]
    else:
        redirect_url = '/404/' + unk_pg_lc

    return redirect(redirect_url, unknown_page=unk_pg_lc)


def not_found(request, unknown_page='default_unk_pg_2'):

    """ Load and render the 404 not found template """

    template = loader.get_template('content/404.html')
    context = {
        'unknown_page': unknown_page,
    }
    return HttpResponse(template.render(context, request))
