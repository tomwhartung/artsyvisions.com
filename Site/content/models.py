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

import codecs
import fnmatch
import json
import os
import re

DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG')
RUNNING_LOCALLY = os.environ.get('RUNNING_LOCALLY', '0')

VISIONS_JSON_DIRECTORY = '/static/content/json/visions/'
DRAFT_VISIONS_JSON_DIRECTORY = '/static/content/json/visions-drafts/'


class VisionsList:

    """
    Gather a list of visions json files for the specified visions_page_name
    Read them and set other, derived values needed for the templates
    """

    def __init__(self, visions_page_name='all'):

        """
        Get a list of visions json files
        Valid values for visions_page_name:
        - person - visions of individuals
        - people - visions of pairs of people
        - groups - visions of groups of people
        - all - default if missing or invalid
        """

        self.visions_page_name = visions_page_name
        #self.visions_files = []
        self.visions_list_data = []

        if RUNNING_LOCALLY != '0':
            self.read_visions_list_data(DRAFT_VISIONS_JSON_DIRECTORY)

        self.read_visions_list_data(VISIONS_JSON_DIRECTORY)


    def get_visions_file_list(self, visions_json_directory):

        """
        Create a list of files containing the data we need
        """

        site_content_dir = os.path.abspath(os.path.dirname(__file__))
        visions_root_dir = site_content_dir + visions_json_directory
        all_visions_files = sorted(os.listdir(visions_root_dir), reverse=True)

        if (self.visions_page_name == 'person' or
            self.visions_page_name == 'people' or
            self.visions_page_name == 'groups'):
            fnmatch_string = '*' + self.visions_page_name + '*'
        else:
            fnmatch_string = '*'

        fnmatch_all_string = '*-all-*'
        filtered_list = []

        for vis_file in all_visions_files:
            matches_all = fnmatch.fnmatch(vis_file, fnmatch_all_string)
            if matches_all:
                filtered_list.append(vis_file)
            else:
                matches_fnmatch = fnmatch.fnmatch(vis_file, fnmatch_string)
                if matches_fnmatch:
                    filtered_list.append(vis_file)

        if DJANGO_DEBUG:
            print('VisionsList - __init__ - self.visions_page_name:', self.visions_page_name)
            #print('VisionsList - __init__ - fnmatch_string:', fnmatch_string)
            print('VisionsList - __init__ - filtered_list:', filtered_list)

        return filtered_list


    def read_visions_list_data(self, visions_json_directory=None):

        """
        Create a list of files containing the data we need
        Create a VisionFile object for each file
        Use the object to get the data needed for the visions list page
        """
        filtered_list = self.get_visions_file_list(visions_json_directory)

        for vis_file in filtered_list:
            ### vis_file_name, vis_file_ext = os.path.splitext(vis_file)
            vision_file_obj = VisionFile(visions_json_directory, vis_file)
            vision_file_obj.set_vision_dict_data()
            vision_dict = vision_file_obj.vision_dict
            self.visions_list_data.append(vision_dict)
            if DJANGO_DEBUG:
                print('VisionsList - read_visions_list_data - vis_file:', vis_file)
                #print('VisionsList - read_visions_list_data - vision_dict:', vision_dict)

        return self.visions_list_data


class VisionStory:

    """
    Gather the data needed for the story specified by vision_file_no_ext
    """

    def __init__(self, vision_file_no_ext='best_one_so_far'):
        """
        Read in the data for a single vision from the vision .json file
        Read in the html for the story and set that in the data
        """
        self.get_visions_story_data(vision_file_no_ext)
        if DJANGO_DEBUG:
            story_html = self.visions_story_data['story_html']
            print('VisionStory - __init__ - story_html:', story_html)


    def get_visions_story_data(self, vision_file_no_ext):

        """
        Read in the data for a single vision from the vision .json file
        Read in the html for the story and set that in the data
        """

        self.visions_story_data = {}
        self.visions_story_data['vision_file_no_ext'] = vision_file_no_ext
        vision_file_name = self.visions_story_data['vision_file_no_ext'] + '.json'
        vision_file_obj = VisionFile(VISIONS_JSON_DIRECTORY, vision_file_name)
        published_file_exists = vision_file_obj.set_vision_dict_data()

        if not published_file_exists:
            vision_file_obj = VisionFile(DRAFT_VISIONS_JSON_DIRECTORY, vision_file_name)
            draft_file_exists = vision_file_obj.set_vision_dict_data()
            if not draft_file_exists:
                story_html = '<p>Unable to find file vision_file_name <q>' \
                    + vision_file_name + '</q>!</p>'
                self.visions_story_data['story_html'] = story_html
                return False

        self.visions_story_data['vision_dict'] = vision_file_obj.vision_dict
        self.vision_file_obj = vision_file_obj
        self.get_story_and_footnotes()
        return self.visions_story_data


    def get_story_and_footnotes(self):
        self.visions_story_data['story_html'] = self.get_story_html()


    def get_story_html(self):
        """
        """
        if 'story_file_name' in self.vision_file_obj.vision_dict:
            story_html_string = self.read_story_html_file()
        else:
            story_html_string = '<p>The story_file_path is not set in the json file.</p>'

        return story_html_string

    def read_story_html_file(self):
        """
        """
        story_file_name = self.vision_file_obj.vision_dict['story_file_name']
        vision_type = self.vision_file_obj.vision_dict['vision_type']
        site_content_dir = os.path.abspath(os.path.dirname(__file__))
        story_file_dir = site_content_dir + '/static/content/html/' + vision_type + '/'
        story_file_path = story_file_dir + story_file_name
        file_exists = os.path.isfile(story_file_path)
        if file_exists:
            story_html_file = codecs.open(story_file_path, encoding='utf-8', mode="r")
            story_html_string = story_html_file.read()
            story_html_file.close()
        else:
            story_html_string = '<p>File missing.</p>'
            story_html_string += '<p>story_file_path: <q>' + story_file_path + '</q></p>'

        return story_html_string



class VisionFile:

    """
    Read in the data for a single vision from a vision .json file
    The passed-in vision_file_name must have the .json filename extension
    """

    def __init__(self, visions_json_directory=None, vision_file_name=None):

        """ Save the passed-in values for use by methods called later """

        self.visions_json_directory = visions_json_directory
        self.vision_file_name = vision_file_name


    def set_vision_dict_data(self):
        """
        Ensure we have the file directory and name, return False if not
        Read it and set the values needed for the template in this object
        If the file exists, return True, else return False
        """

        self.vision_dict = {}
        if self.visions_json_directory == None or self.vision_file_name == None:
            return False
        else:
            file_exists = self.read_visions_file()
            if file_exists:
                self.vision_dict['vision_file_name'] = self.vision_file_name
                self.vision_dict['vision_file_no_ext'] = os.path.splitext(self.vision_file_name)[0]
                self.set_vision_type()   # must call this one first!
                self.set_group_name()
                self.set_defaults()
                self.set_image_data()
            return file_exists


    def read_visions_file(self):
        """
        (Try to) read in all the json for the passed-in vision_file_name
        If the file exists, return True, else return False
        """
        site_content_dir = os.path.abspath(os.path.dirname(__file__))
        data_file_dir = site_content_dir + self.visions_json_directory
        vision_file_path = data_file_dir + self.vision_file_name
        file_exists = os.path.isfile(vision_file_path)
        if file_exists:
            vision_json_file = open(vision_file_path, encoding='utf-8', mode="r")
            vision_json_string = vision_json_file.read()
            vision_json_file.close()
            self.vision_dict = json.loads(vision_json_string)
            return True
        else:
            return False


    def set_vision_type(self):
        """
        Get the vision_type from the vision_file_name, which is of the form:
            9999-{vision_type}-{name_or_names}.json
        vision_type = 'person' , 'people' , or 'groups'
        """

        pattern = re.compile('\d\d\d\d-(\w+)-')
        match = re.search(pattern, self.vision_file_name)
        vision_type = match.group(1)

        self.vision_dict['vision_type'] = vision_type
        return vision_type


    def set_group_name(self):
        """
        If it's a group file,
            get the group_name from the vision_file_name
        The vision_file_name is of the form:
            9999-{vision_type}-{name_or_names}.json
        When vision_type = 'groups',
            the "name_or_names" part is the group_name
        NOTE: this method uses the vision_type so make sure it is set!
        """

        if self.vision_dict['vision_type'] == 'groups':
            pattern = re.compile('-groups-(\w+).json')
            match = re.search(pattern, self.vision_file_name)
            group_name = match.group(1)
            self.vision_dict['group_name'] = group_name
        else:
            self.vision_dict['group_name'] = ''
        return self


    def set_defaults(self):
        """
        If any of the author, date, or disclsure_* parameters are not set,
            Set an appropriate default value
        """

        DEFAULT_DISCLOSURE_TEXT = \
            'This page may contain affiliate marketing links, ' + \
            'which help cover the cost of creating and maintaining this site.'

        if 'author' not in self.vision_dict or self.vision_dict['author'] == "":
            self.vision_dict['author'] = 'Tom Hartung'
        if 'date' not in self.vision_dict or self.vision_dict['date'] == "":
            self.vision_dict['date'] = '2018'
        if 'disclosure_text' not in self.vision_dict \
         or self.vision_dict['disclosure_text'] == "":
            self.vision_dict['disclosure_text'] = DEFAULT_DISCLOSURE_TEXT
        if 'disclosure_btn_text' not in self.vision_dict \
         or self.vision_dict['disclosure_btn_text'] == "":
            self.vision_dict['disclosure_btn_text'] = 'Full Explanation'



    def set_image_data(self):
        """
        Derive and set values for the image_file_path in the vision_dict
        NOTE: this method uses the vision_type and group_name (if it's a group)
            so make sure they are both set!
        """
        vision_type = self.vision_dict['vision_type']
        image_file_parent_dir = 'content/images/visions/' + vision_type + '/'
        if (self.vision_dict['vision_type'] == 'person' or
            self.vision_dict['vision_type'] == 'people'):
            image_file_path = image_file_parent_dir + self.vision_dict['image_file_name']
            self.vision_dict['image_file_path'] = image_file_path
        elif self.vision_dict['vision_type'] == 'groups':
            image_data = []
            group_name = self.vision_dict['group_name']
            for img_dict in self.vision_dict['image_file_list']:
                img_fn = img_dict['image_file_name']
                image_file_path = image_file_parent_dir + group_name + '/' + img_fn
                image_file_dict = {}
                image_file_dict['name'] = img_dict['name']
                image_file_dict['image_file_path'] = image_file_path
                image_data.append(image_file_dict)
            self.vision_dict['image_data'] = image_data
        return self
