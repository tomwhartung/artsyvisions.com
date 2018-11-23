""" urls.py for our content app

Purpose: define the urls for this app
Author: Tom W. Hartung
Date: Summer, 2018.
Copyright: (c) 2018 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
    https://docs.djangoproject.com/en/2.1/intro/tutorial01/#write-your-first-view
"""

from django.conf.urls import *

from . import views

"""
When upgrading to django 2.0+, we can use the path method:
    https://docs.djangoproject.com/en/2.0/ref/urls/#path

from django.urls import path

The routes we are using are quite simple, and we already have a
version of this file that uses the path method:
    ./urls-uses_path-save_for_2.0.py
More:
    https://stackoverflow.com/questions/47947673/is-it-better-to-use-path-or-url-in-urls-py-for-django-2-0
"""

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^index$', views.index, name='index'),
    url(r'^v$', views.versions, name='versions'),
    url(r'^visions/all$',
        views.visions_all,
        name='visions_all'),
    url(r'^visions/person$',
        views.visions_person,
        name='visions_person'),
    url(r'^visions/pairs$',
        views.visions_pairs,
        name='visions_pairs'),
    url(r'^visions/groups$',
        views.visions_groups,
        name='visions_groups'),
    url(r'^visions/story/$',
        views.visions_story,
        name='visions_story'),
    url(r'^visions/story/(?P<vision_file_no_ext>\S+)$',
        views.visions_story,
        name='visions_story'),
    url(r'^legal/affiliate_marketing_disclosure$',
        views.affiliate_marketing_disclosure,
        name='affiliate_marketing_disclosure'),
    url(r'^legal/privacy_policy$',
        views.privacy_policy,
        name='privacy_policy'),
    url(r'^legal/questionnaire_disclaimer$',
        views.questionnaire_disclaimer,
        name='questionnaire_disclaimer'),
    url(r'^legal/terms_of_service$',
        views.terms_of_service,
        name='terms_of_service'),
    url(r'^<path:unknown_page>$',
        views.not_found,
        name='not_found'),

]
