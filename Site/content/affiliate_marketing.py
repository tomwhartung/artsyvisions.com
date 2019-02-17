""" Module to manage affiliate marketing links

Purpose: allow managing affiliate marketing links in one place
Author: Tom W. Hartung
Date: Winter, 2019
Copyright: (c) 2019 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:

"""


class AffiliateLinks:

    """
    Use python dictionaries to make it easier to update affiliate links
    """

    #
    # Source Link Dictionaries:
    #
    afl_default = {
        'ah_by_chernow': 'https://groja.com/conversion/afl_default',
        'ah_ax_video': 'https://groja.com/conversion/afl_default',
        'citizen_kane': 'https://groja.com/conversion/afl_default',
        'concerning_by_kandinsky': 'https://groja.com/conversion/afl_default',
        'fawlty_towers': 'https://groja.com/conversion/afl_default',
        'game_of_thrones': 'https://groja.com/conversion/afl_default',
        'im_video': 'https://groja.com/conversion/afl_default',
        'ph_kukla': 'https://groja.com/conversion/afl_default',
        'star_trek_tos': 'https://groja.com/conversion/afl_default',
        'tj_himself': 'https://groja.com/conversion/afl_default',
        'tj_by_burns': 'https://groja.com/conversion/afl_default',
        'twin_peaks': 'https://groja.com/conversion/afl_default',
        'weirdsville_usa': 'https://groja.com/conversion/afl_default',
        'wild_at_heart': 'https://groja.com/conversion/afl_default',
        'wild_heart_book': 'https://groja.com/conversion/afl_default',
        'wire': 'https://groja.com/conversion/afl_default',
        'x_files': 'https://groja.com/conversion/afl_default',
        'xxx': 'https://groja.com/conversion/afl_default',
    }

    afl_none = {
        'ah_by_chernow': '',
        'ah_ax_video': '',
        'citizen_kane': '',
        'concerning_by_kandinsky': '',
        'fawlty_towers': '',
        'game_of_thrones': '',
        'im_video': '',
        'ph_kukla': '',
        'star_trek_tos': '',
        'tj_himself': '',
        'tj_by_burns': '',
        'twin_peaks': '',
        'weirdsville_usa': '',
        'wild_at_heart': '',
        'wild_heart_book': '',
        'wire': '',
        'x_files': '',
        'xxx': '',
    }

    #
    # Active Link Dictionaries:
    #
    afl_content = {}
    afl_button = {}

    def __init__(self):

        """
        Assign source links to active links
        """

        self.afl_content['ah_by_chernow'] = self.afl_default['ah_by_chernow']
        self.afl_button['ah_by_chernow'] = self.afl_default['ah_by_chernow']
        self.afl_content['ah_ax_video'] = self.afl_default['ah_ax_video']
        self.afl_button['ah_ax_video'] = self.afl_default['ah_ax_video']

        self.afl_content['citizen_kane'] = self.afl_default['citizen_kane']
        self.afl_button['citizen_kane'] = self.afl_default['citizen_kane']

        self.afl_content['concerning_by_kandinsky'] \
            = self.afl_default['concerning_by_kandinsky']

        self.afl_content['fawlty_towers'] = self.afl_default['fawlty_towers']
        self.afl_button['fawlty_towers'] = self.afl_default['fawlty_towers']

        self.afl_content['game_of_thrones'] = self.afl_default['game_of_thrones']
        self.afl_button['game_of_thrones'] = self.afl_default['game_of_thrones']

        self.afl_content['im_video'] = self.afl_default['im_video']

        self.afl_content['ph_kukla'] = self.afl_default['ph_kukla']
        self.afl_button['ph_kukla'] = self.afl_default['ph_kukla']

        self.afl_content['star_trek_tos'] = self.afl_default['star_trek_tos']
        self.afl_button['star_trek_tos'] = self.afl_default['star_trek_tos']


        self.afl_content['tj_himself'] = self.afl_default['tj_himself']
        self.afl_button['tj_himself'] = self.afl_default['tj_himself']
        self.afl_content['tj_by_burns'] = self.afl_default['tj_by_burns']
        self.afl_button['tj_by_burns'] = self.afl_default['tj_by_burns']

        self.afl_content['wire'] = self.afl_default['wire']
        self.afl_button['wire'] = self.afl_default['wire']

        self.afl_content['x_files'] = self.afl_default['x_files']
        self.afl_button['x_files'] = self.afl_default['x_files']


        self.afl_content['twin_peaks'] = self.afl_default['twin_peaks']
        self.afl_button['twin_peaks'] = self.afl_default['twin_peaks']
        self.afl_content['wild_at_heart'] = self.afl_default['wild_at_heart']
        self.afl_button['wild_at_heart'] = self.afl_default['wild_at_heart']
        self.afl_content['wild_heart_book'] = self.afl_default['wild_heart_book']
        self.afl_button['wild_heart_book'] = self.afl_default['wild_heart_book']
        self.afl_content['weirdsville_usa'] = self.afl_default['weirdsville_usa']
        self.afl_button['weirdsville_usa'] = self.afl_default['weirdsville_usa']

        self.afl_content['xxx'] = self.afl_default['xxx']
        self.afl_button['xxx'] = self.afl_default['xxx']
