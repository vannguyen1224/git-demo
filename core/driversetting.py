'''
Created on Jun 9, 2016

@author: thanh.viet.le
'''

from common.constant import Browser
from common.constant import Platform

class DriverSetting(object):

    def __init__(self, browser_name = Browser.Firefox, platform = Platform.WINDOWS, element_wait_timeout = 180, hub_url = None):
        self.browser_name = browser_name
        self.platform = platform
        self.element_wait_timeout = element_wait_timeout
        self.hub_url = hub_url
        