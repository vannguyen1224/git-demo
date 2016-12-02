'''
Created on Jun 15, 2016

@author: thanh.viet.le
'''
from selenium.webdriver.common.by import By
from core.element import Element

class EditableCombobox(Element):      
    def select(self, value):
        self._element.click()        
        if("@" in value):
            value = value.lower()
        
        input_elem = Element(self._element.wrapped_element.find_element(By.XPATH, "../following-sibling::input[1]"), self._driver)        
        input_elem.send_keys(value)
        self._driver.find_element(By.XPATH, u"//a/span[contains(text(), '{}')]".format(value)).click()
