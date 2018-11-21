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
    path('index', views.index, name='index'),
    path('visions/all',
        views.visions_all,
        name='visions_all'),
    path('visions/person',
        views.visions_person,
        name='visions_person'),
    path('visions/pairs',
        views.visions_pairs,
        name='visions_pairs'),
    path('visions/groups',
        views.visions_groups,
        name='visions_groups'),
    path('visions/story/',
        views.visions_story,
        name='visions_story'),
    path('visions/story/<vision_file_no_ext>',
        views.visions_story,
        name='visions_story'),
    path('legal/affiliate_marketing_disclosure',
        views.affiliate_marketing_disclosure,
        name='affiliate_marketing_disclosure'),
    path('legal/privacy_policy',
        views.privacy_policy,
        name='privacy_policy'),
    path('legal/questionnaire_disclaimer',
        views.questionnaire_disclaimer,
        name='questionnaire_disclaimer'),
    path('legal/terms_of_service',
        views.terms_of_service,
        name='terms_of_service'),
    path('<path:unknown_page>',
        views.not_found,
        name='not_found'),

]
