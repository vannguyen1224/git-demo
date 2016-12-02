'''
Created on May 30, 2016

@author: thanh.viet.le
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from core.element import Element
from common.constant import Browser, Constant
from common.stopwatch import Stopwatch
import os, re, platform
from core.editable_combobox import EditableCombobox

class Driver(object):
    
    _driver = None
    _element_wait_timeout = 0
       
    def __init__(self, driverSetting):
        self._element_wait_timeout = driverSetting.element_wait_timeout
        self._driverSetting = driverSetting
        
        if(driverSetting.hub_url == None):  # Local WebDriver
            if(driverSetting.browser_name == Browser.Firefox):
                self._driver = webdriver.Firefox()
            elif(driverSetting.browser_name == Browser.IE):
                file_path = os.path.dirname(os.path.dirname(__file__)) + "\\libs\\IEDriverServer.exe"
                self._driver = webdriver.Ie(file_path)
            elif(driverSetting.browser_name == Browser.Safari):
                self._driver = webdriver.Safari()
        else:  # Remote WebDriver
            if(driverSetting.browser_name == Browser.Firefox):
                capabilities = DesiredCapabilities.FIREFOX.copy()                                
            elif(driverSetting.browser_name == Browser.IE):
                capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
            elif(driverSetting.browser_name == Browser.Safari):
                capabilities = DesiredCapabilities.SAFARI.copy()       
            
            capabilities['platform'] = driverSetting.platform
            self._driver = webdriver.Remote(command_executor=driverSetting.hub_url, desired_capabilities=capabilities)
        
        self._driver.set_page_load_timeout(driverSetting.element_wait_timeout)
        self._driver.implicitly_wait(1)
        
        # Update run environment file at data\RunEnv.txt
        self._update_run_env(driverSetting)
    
    @property
    def driverSetting(self):
        return self._driverSetting
    
    """All Web_driver's methods"""
    def _update_run_env(self, driverSetting):
        delim = "="
        new_line = "\n"
        space = " "
        slash = "/"
        
        # Get browser name & version
        os_name = machine_name = browser = ""
        
        if(driverSetting.hub_url == None):
            os_name = platform.platform()
            machine_name = platform.node()
            browser = str(self._driver.capabilities["browserName"]).capitalize() + ", version " + self._driver.capabilities["version"] 
        else:
            sys_info = self.execute_script("return window.navigator.userAgent")
            os_name = re.search("\((.+?)\;", sys_info).group(1)
            items = sys_info.split(space)
            browser = items[len(items) - 1].replace(slash, ", version ")
        # Write information 
        file_env = open(Constant.RunEnvironmentFile, 'w')
        file_env.truncate()
        file_env.write("os" + delim + os_name + new_line)
        file_env.write("machine" + delim + machine_name + new_line)
        file_env.write("browser" + delim + browser)
        file_env.close()
    
    def execute_script(self, script, *args):
        result = self._driver.execute_script(script, *args)
        return result
    
    def get(self, url):        
        self._driver.get(url)
    
    def _find_element(self, by = By.ID, value = None, timeout = None):    
        print("Finding element {By: %s, Value: %s}" % (by, value))                 
       
        if(timeout == None):
            timeout = self._element_wait_timeout
            
        sw = Stopwatch()
        sw.start()
        
        if(sw.elapsed().total_seconds() < timeout):
            try:
                #return WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable((by, value)))
                return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located((by, value)))
            except StaleElementReferenceException:
                return self._find_element(by, value, timeout - sw.elapsed().total_seconds())
            except TimeoutException:
                return None
            except Exception as e:
                raise(e)                
        
        return None
    
    def wait_for_element_invisible(self, by = By.ID, value = None, timeout = None):
        self.is_element_invisible(by, value, timeout)
    
    def wait_for_element_visible(self, by = By.ID, value = None, timeout = None):
        self.is_element_visible(by, value, timeout)
        
    def is_element_visible(self, by = By.ID, value = None, timeout = None):
        if(self._find_element(by, value, timeout) != None):
            return True
        else:
            return False
    
    def is_element_invisible(self, by = By.ID, value = None, timeout = None):
        print("Finding element {By: %s, Value: %s}" % (by, value)) 
        if(timeout == None):
            timeout = self._element_wait_timeout
        
        return WebDriverWait(self._driver, timeout).until(EC.invisibility_of_element_located((by, value)))
    
    def find_element(self, by = By.ID, value = None, timeout = None):
        elem = self._find_element(by, value, timeout)
        return Element(elem, self)
    
    def find_editable_combobox(self, by = By.ID, value = None, timeout = None):
        elem = self.find_element(by, value, timeout)       
        return EditableCombobox(elem, self)        
    
    def _find_elements(self, by = By.ID, value = None, timeout = None):
        if(timeout == None):
            timeout = self._element_wait_timeout
            
        sw = Stopwatch()
        sw.start()
        
        if(sw.elapsed().total_seconds() < timeout):
            try:
                return WebDriverWait(self._driver, timeout).until(EC.presence_of_all_elements_located((by, value)))                           
            except StaleElementReferenceException:               
                return self._find_elements(by, value, timeout - sw.elapsed().total_seconds())
            except TimeoutException:
                return None
            except Exception as e:
                raise(e)                
        
        return None  
    
    def find_elements(self, by = By.ID, value = None, timeout = None):
        found_elems = []
        elems = self._find_elements(by, value, timeout)
        
        if(elems != None):            
            for elem in elems:
                found_elems.append(Element(elem))
            
        return found_elems
    
    def get_dialog_message(self, close_dialog = True):
        result = self._driver.switch_to_alert().text
        
        if(close_dialog == True):
            self.handle_dialog(close_dialog)
        
        return result    
    
    def handle_dialog(self, accept = False):
        if(accept == True):
            self._driver.switch_to_alert().accept()
        else:
            self._driver.switch_to_alert().dismiss()
    
    def maximize_window(self):
        self._driver.maximize_window()
        
    def close(self):
        self._driver.close()
    
    def quit(self):        
        self._driver.quit()
    
    def switch_to_main_window(self):
        self.switch_to_window(0)

    def switch_to_window(self, index = 0):
        self._driver.switch_to.window(self.window_handles[index])
        self.switch_to_default_content()
    
    def switch_to_default_content(self):
        self._driver.switch_to.default_content()
    
    def switch_to_frame(self, frame_id):
        self._driver.switch_to.frame(frame_id)
    
    def save_screenshot(self, filename):
        return self._driver.save_screenshot(filename)
    
    """ Properties """
    @property
    def wrapped_driver(self):
        return self._driver
    
    @property
    def title(self):
        return self._driver.title
    
    @property
    def current_url(self):
        return self._driver.current_url
    
    @property
    def window_handles(self):
        return self._driver.window_handles
