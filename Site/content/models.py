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
        - pairs - visions of pairs of people
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
            self.visions_page_name == 'pairs' or
            self.visions_page_name == 'groups'):
            fnmatch_string = '*' + self.visions_page_name + '*.json'
        else:
            fnmatch_string = '*.json'

        fnmatch_all_string = '*-all-*.json'
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
            if DJANGO_DEBUG and RUNNING_LOCALLY != '0':
                print('VisionsList - read_visions_list_data - vis_file:', vis_file)
                #print('VisionsList - read_visions_list_data - vision_dict:', vision_dict)
            vision_file_obj = VisionFile(visions_json_directory, vis_file)
            vision_file_obj.set_vision_dict_data()
            vision_dict = vision_file_obj.vision_dict
            self.visions_list_data.append(vision_dict)

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


    def get_visions_story_data(self, vision_file_no_ext):
        """
        Read in the data for a single vision from the vision .json file
        Read in the html for the story and set that in the data
        """

        self.visions_story_data = {}
        self.visions_story_data['vision_file_no_ext'] = vision_file_no_ext

        """
        For the "index" route, use hard-coded values set in a special fcn,
        else get them from the json file
        """
        if vision_file_no_ext == 'index':
            self.visions_story_data = self.set_story_data_for_index()
            return self.visions_story_data
        else:
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
        self.visions_story_data['story_html'] = self.get_story_html()
        self.visions_story_data['notes_html'] = self.get_notes_html()
        return self.visions_story_data


    def get_story_html(self):

        """ Read the story file and return the html """

        if 'story_file_name' in self.vision_file_obj.vision_dict:
            file_name = self.vision_file_obj.vision_dict['story_file_name']
            if len(file_name) > 5:
                html_from_file = self.read_html_file(file_name)
                #story_html_string = self.add_new_row_markup(html_from_file)
                story_html_string = html_from_file
            else:
                story_html_string = '<p>Invalid story_file_name: '
                story_html_string += '<q>' + '</q></p>'
        else:
            story_html_string = '<p>No story_file_name in the json file.</p>'

        return story_html_string


    def add_new_row_markup(self, html_from_file):

        """
            *** DEPRECATED ***
            Add html for new rows to the story html, as appropriate
            Keeping the cruft around in case we change our mind back again
            *** DEPRECATED - DELETE ME YOU WUSS ***
        """

        NEW_ROW_MATCH_STRING = '<< NEW_ROW_MARKUP >>'
        NEW_ROW_MARKUP = """
     </div><!-- .story-html-inner -->
    </div><!-- .story-html-outer -->
   </div><!-- .col -->
  </div><!-- .row -->
  <div class="row">
   <div class="col s12 m12 l12">
    <div class="story-html-outer z-depth-3">
     <div class="story-html-inner hoverable">
        """

        new_row_pattern = re.compile(NEW_ROW_MATCH_STRING)
        story_html_string = new_row_pattern.sub(NEW_ROW_MARKUP, html_from_file)

        return story_html_string


    def get_notes_html(self):

        """ Read the notes file, if there is one, and return the html """

        notes_html_string = ''

        if 'notes_file_name' in self.vision_file_obj.vision_dict:
            file_name = self.vision_file_obj.vision_dict['notes_file_name']
        else:
            file_name = ''

        if len(file_name) > 5:
            notes_html_string = self.read_html_file(file_name)

        return notes_html_string


    def read_html_file(self, file_name):
        """
        Try to read the html in the specified file,
        If successful, return the html, else return an error message
        """

        vision_type = self.vision_file_obj.vision_dict['vision_type']
        site_content_dir = os.path.abspath(os.path.dirname(__file__))
        directory = site_content_dir + '/static/content/html/' + vision_type
        file_path = directory + '/' + file_name
        file_exists = os.path.isfile(file_path)
        if file_exists:
            html_file = codecs.open(file_path, encoding='utf-8', mode="r")
            html_string = html_file.read()
            html_file.close()
        else:
            html_string = '<p>Html file missing.</p>'
            html_string += '<p>file_path: <q>' + file_path + '</q></p>'

        return html_string


    def set_story_data_for_index(self):

        """
        Set data normally in the json file to hard-coded values that
        allow us to see the html templates by accessing '/index'
        """

        self.vision_file_obj = VisionFile()
        self.vision_file_obj.vision_dict = {}
        self.vision_file_obj.vision_dict['story_file_name'] = 'body.html'
        self.vision_file_obj.vision_dict['notes_file_name'] = 'notes.html'
        self.vision_file_obj.vision_dict['vision_type'] = 'templates'
        self.vision_file_obj.vision_dict['title'] = 'index'
        self.vision_file_obj.vision_dict['subtitle_html'] = 'html/templates/*'
        self.vision_file_obj.vision_dict['author'] = 'Mr. Templates Person'
        self.vision_file_obj.vision_dict['date'] = '2018'
        self.vision_file_obj.vision_dict['disclosure_text'] = 'Disclosure Text'
        self.vision_file_obj.vision_dict['disclosure_btn_text'] = 'Button Text'

        self.visions_story_data = {}
        self.visions_story_data['vision_dict'] = self.vision_file_obj.vision_dict
        self.visions_story_data['story_html'] = self.get_story_html()
        self.visions_story_data['notes_html'] = self.get_notes_html()
        return self.visions_story_data


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
            vision_json_file = codecs.open(vision_file_path, encoding='utf-8', mode="r")
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
        vision_type = 'person' , 'pairs' , or 'groups'
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
            pattern = re.compile('-groups-([-\w]+).json')
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

        if 'title' not in self.vision_dict or self.vision_dict['title'] == "":
            self.vision_dict['title'] = '[No Title]'
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
            self.vision_dict['vision_type'] == 'pairs'):
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
