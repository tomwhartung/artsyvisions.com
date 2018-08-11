##
## from django.shortcuts import render
##
## # Create your views here.

#
# From "Write your first view" in:
# https://docs.djangoproject.com/en/2.1/intro/tutorial01/#write-your-first-view
#
from django.http import HttpResponse


def index(request):
        return HttpResponse("Hello, world. You're at the content index.")

