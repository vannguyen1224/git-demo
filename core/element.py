'''
Created on May 30, 2016

@author: thanh.viet.le
'''

from selenium import webdriver

class Element(object):

    def __init__(self, webelement, driver):        
        self._element = webelement
        self._driver = driver
    
    def click(self):
        try:
            if(self._element == None):
                raise Exception("Element is None!")
            else:
                self._element.click()
        except Exception as ex:
            print("Cannot click Element. Error: {}".format(ex))
            raise    
    
    def jsclick(self):
        try:
            if(self._element == None):
                raise Exception("Element is None!")
            else:
                self._driver.execute_script("arguments[0].click();", self._element)     
        except Exception as ex:
            print("Cannot click Element. Error: {}".format(ex))
            raise     
    
    def submit(self):
        try:
            if(self._element == None):
                raise Exception("Element is None!")
            else:
                self._element.submit()
        except Exception as ex:
            print("Cannot submit Element. Error: {}".format(ex))            
            raise
        
    def clear(self):
        try:
            if(self._element == None):
                raise Exception("Element is None!")
            else:
                self._element.clear()
        except Exception as ex:
            print("Cannot clear Element. Error: {}".format(ex))
            raise
    
    def send_keys(self, *value):
        try:
            if(self._element == None):
                raise Exception("Element is None!")
            else:
                self._element.send_keys(*value)
        except Exception as ex:
            print("Cannot send keys to Element. Error: {}".format(ex))
            raise
        
    def type(self, *value):
        self.clear()
        self.send_keys(*value)
        
    def get_attribute(self, name):
        try:
            if(self._element == None):
                raise Exception("Element is None!")
            else:
                return self._element.get_attribute(name)
        except Exception as ex:
            print("Cannot get attribute of Element. Error: {}".format(ex))
            raise     

    def is_selected(self):
        try:
            if(self._element == None):
                raise Exception("Element is None!")
            else:
                return self._element.is_selected()
        except Exception as ex:
            print("Cannot get is_selected attribute of Element. Error: {}".format(ex))
            raise
        
    def is_enabled(self):
        try:
            if(self._element == None):
                raise Exception("Element is None!")
            else:
                return self._element.is_enabled()
        except Exception as ex:
            print("Cannot get is_enabled attribute of Element. Error: {}".format(ex))
            raise
    
    def is_displayed(self):
        try:
            if(self._element == None):
                return False
            else:
                return self._element.is_displayed()
        except Exception as ex:
            print("Cannot get is_displayed attribute of Element. Error: {}".format(ex))
            return False  

    """ Properties """
    @property
    def tag_name(self):
        if(self._element != None):
            return self._element.tag_name
        else:
            return None
        
    @property
    def text(self):
        if(self._element != None):
            return self._element.text
        else:
            return None

    @property
    def screenshot_as_base64(self):
        if(self._element != None):
            return self._element.screenshot_as_base64()
        else:
            return None
        
    @property
    def screenshot_as_png(self):
        if(self._element != None):
            return self._element.screenshot_as_png()
        else:
            return None

    @property
    def parent(self):
        if(self._element != None):
            return self._element.parent()
        else:
            return None

    @property
    def wrapped_element(self):
        return self._element
    
    @property
    def id(self):
        if(self._element != None):
            return self._element.id()
        else:
            return None
    
    """Extension methods"""
    def mouse_to(self):
        try:
            if(self._element == None):
                raise Exception("Element is None!")
            else:
                webdriver.ActionChains(self._driver.wrapped_driver).move_to_element(self._element).perform()
        except Exception as ex:
            print("Cannot move mouse to Element. Error: {}".format(ex))
            raise
            
    def check(self):
        if(self.is_selected() == False):
            self._element.click()
    
    def uncheck(self):
        if(self.is_selected() == True):
            self._element.click()
            