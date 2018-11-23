"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import *

"""
When upgrading to django 2.0+, we can use the path method:
    https://docs.djangoproject.com/en/2.0/ref/urls/#path

from django.urls import include, path

The routes we are using are quite simple, and we already have a
version of this file that uses the path method:
    ./urls-uses_path-save_for_2.0.py
More:
    https://stackoverflow.com/questions/47947673/is-it-better-to-use-path-or-url-in-urls-py-for-django-2-0
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('content.urls')),
]
