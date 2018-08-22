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
import re

DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG')
RUNNING_LOCALLY = os.environ.get('RUNNING_LOCALLY')


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
        all_visions_files = sorted(os.listdir(visions_root_dir))

        if (visions_page_name == 'person' or
            visions_page_name == 'people' or
            visions_page_name == 'groups'):
            fnmatch_string = '*' + visions_page_name +'*'
        else:
            fnmatch_string = '*'

        self.visions_files = []
        for vis_file in all_visions_files:
            if fnmatch.fnmatch(vis_file, fnmatch_string):
                self.visions_files.append(vis_file)

        if DJANGO_DEBUG:
            print('VisionsList - __init__ - visions_page_name:', visions_page_name)
            print('VisionsList - __init__ - fnmatch_string:', fnmatch_string)
            print('VisionsList - __init__ - self.visions_files:', self.visions_files)

        self.visions_list_data = []


    def set_visions_list_data(self):

        """
        Get the data needed to render the visions list page
        """

        for vis_file in self.visions_files:
            ### vis_file_name, vis_file_ext = os.path.splitext(vis_file)
            vision_file_obj = VisionFile(vis_file)
            vision_file_obj.set_list_data()
            vis_dict = vision_file_obj.vision_dict
            self.visions_list_data.append(vis_dict)
            if DJANGO_DEBUG:
                print('VisionsList - set_visions_list_data - vis_file:', vis_file)
                print('VisionsList - set_visions_list_data - vis_dict:', vis_dict)

        return self.visions_list_data


class VisionFile:

    """
    Read in the data for a single vision from a vision .json file
    The passed-in vision_file_name must have the .json filename extension
    """

    def __init__(self, vision_file_name=None):
        """ Read in all the json for the passed-in vision_file_name """
        self.vision_file_name = vision_file_name
        if vision_file_name == None:
            self.visions_dict = {}
        else:
            print('VisionFile - __init__ - vision_file_name:', vision_file_name)
            site_content_dir = os.path.abspath(os.path.dirname(__file__))
            data_file_dir = site_content_dir + VisionsList.VISIONS_DIRECTORY
            data_file_path = data_file_dir + vision_file_name
            vision_json_file = open(data_file_path, encoding='utf-8', mode="r")
            vision_json_string = vision_json_file.read()
            vision_json_file.close()
            self.vision_dict = json.loads(vision_json_string)


    def set_list_data(self):
        """ Set the values needed for the template in this object """
        self.vision_dict['vision_file_name'] = self.vision_file_name
        self.set_vision_type()   # must call this one first!
        self.set_group_name()
        self.set_image_path_values()


    def set_vision_type(self):
        """
        Get the vision_type from the vision_file_name, which is of the form:
            9999-{vision_type}-{name_or_names}.json
        vision_type = 'person' , 'people' , or 'groups'
        """

        # For now, we can keep it simple, but someday, we may need a regex
        # pattern = re.compile('')

        vision_type = self.vision_file_name[5:11]
        self.vision_dict['vision_type'] = vision_type


    def set_group_name(self):
        """
        If it's a group file,
            get the group_name from the vision_file_name
        The vision_file_name is of the form:
            9999-{vision_type}-{name_or_names}.json
        When vision_type = 'groups',
            the "name_or_names" part is the group_name
        """

        if self.vision_dict['vision_type'] == 'groups':
            pattern = re.compile('-groups-(\w+).json')
            match = re.search(pattern, self.vision_file_name)
            group_name = match.group(1)
            self.vision_dict['group_name'] = group_name
        else:
            self.vision_dict['group_name'] = ''


    def set_image_path_values(self):
        """
        Set derived values for the image_file_name or in the image_list,
        as appropriate, in the vision_dict
        NOTE: this method uses the vision_type so make sure it's set!
        """
        vision_type = self.vision_dict['vision_type']
        image_file_parent_dir = 'content/images/visions/' + vision_type + '/'
        print('VisionFile - set_image_path_values - self.vision_dict: ', self.vision_dict)
        print('VisionFile - set_image_path_values - self.vision_dict[image_file_name]: ', self.vision_dict['image_file_name'])
        if self.vision_dict['vision_type'] == 'groups':
            new_image_file_list = []
            group_name = self.vision_dict['group_name']
            print('VisionFile - set_image_path_values - self.vision_dict[image_file_list] BEFORE', self.vision_dict['image_file_list'])
            for img_fn in self.vision_dict['image_file_list']:
                new_img_fn = image_file_parent_dir + group_name + '/' + img_fn
                new_image_file_list.append(new_img_fn)
            self.vision_dict['image_file_list'] = new_image_file_list
            print('VisionFile - set_image_path_values - self.vision_dict[image_file_list] AFTER', self.vision_dict['image_file_list'])
        else:
            new_file_name = image_file_parent_dir + self.vision_dict['image_file_name']
            self.vision_dict['image_file_name'] = new_file_name
            ### image_dict['image_file_path'] = image_file_parent_dir \
            ###     + image_dict['image_file_name']
        return self
