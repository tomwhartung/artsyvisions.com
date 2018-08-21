""" Contains the non-database models for our app.

Purpose: contains the models for unsaved data and read-only data in json format
Author: Tom W. Hartung
Date: Summer, 2018.
Copyright: (c) 2018 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
      (none, yet)
"""

### from django.db import models
### # Create your models here.

import fnmatch
import json
import os

DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG')

class VisionsList:

    """
    Gather a list of visions json files appropriate for the optional
    specified visions_page_name and ...
    ________________________________
    """

    VISIONS_DIRECTORY = '/static/content/json/visions/'

    def __init__(self, visions_page_name='all'):

        """
        Get a list of visions json files
        Valid values for visions_page_name:
        - person - visions of individuals
        - people - visions of pairs of people
        - groups - visions of groups of people
        - all - default if missing or invalid
        """

        site_content_dir = os.path.abspath(os.path.dirname(__file__))
        visions_root_dir = site_content_dir + self.VISIONS_DIRECTORY
        visions_files = sorted(os.listdir(visions_root_dir))

        if (visions_page_name == 'person' or
            visions_page_name == 'people' or
            visions_page_name == 'groups'):
            fnmatch_string = '*' + visions_page_name +'*'
        else:
            fnmatch_string = '*'

        self.visions_files = []
        for vis_file in visions_files:
            if fnmatch.fnmatch(vis_file, fnmatch_string):
                self.visions_files.append(vis_file)

        if DJANGO_DEBUG:
            print('VisionsList - __init__ - visions_page_name:', visions_page_name)
            print('VisionsList - __init__ - fnmatch_string:', fnmatch_string)
            print('VisionsList - __init__ - visions_files:', visions_files)
            print('VisionsList - __init__ - self.visions_files:', self.visions_files)
        self.visions_list_data = []


    def set_visions_list_data(self):

        """
        Get the data needed to render the visions list page
        """

        self.galleries_list_data = []
        return self.galleries_list_data
