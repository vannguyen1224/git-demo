'''
Created on Sep 12, 2016

@author: tien.anh.nguyen
'''
import win32com.client
from time import sleep

def choose_file(self, btnChooseFile, file_path):
    shell = win32com.client.Dispatch("WScript.Shell")
           
    btnChooseFile.click()
#         WebDriverWait(self._driver.wrapped_driver, 15).until(EC.alert_is_present(), "Time out waiting for alert dialog.")
#         alert = self._driver.switch_to_alert();        
#         alert.send_keys(file_path)
    
    sleep(2) # wait for dialog appeared        
    shell.SendKeys(file_path)
    sleep(2) # do not remove this line        
    shell.SendKeys("~")
    shell.SendKeys("~")