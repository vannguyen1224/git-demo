'''
Created on Jun 1, 2016

@author: thanh.viet.le
'''

import os
import string
import random
from data import testdata
from data import setting
from core.driversetting import DriverSetting

class Helper(object):

    @staticmethod
    def generate_random_string(length = 10):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    
    @staticmethod
    def generate_random_email(domain = "mailinator.com"):
        return ("{}{}@{}".format(Helper.generate_random_string(10), "logigear", domain)).lower()
    
    @staticmethod
    def get_data_from_csv_file(data_file_name):
        # Define constant
        csv_delim = ","
        end_line = "\n"
        
        # Read file and put to array
        file_path = os.path.dirname(testdata.__file__)
        f_stream = open(file_path + "\\" + data_file_name, "r")
        lines = f_stream.readlines()
        f_stream.close()
        
        # Get items from lines
        item = []
        result = []
        for i in range (1, len(lines)):
            lines[i] = lines[i].replace(end_line, "")
            item = lines[i].split(csv_delim)
            result.append(item)

        return result
    
    @staticmethod
    def load_execution_setting():
        driverSetting = DriverSetting()
        
        # Define constant
        delim = "="
        end_line = "\n"
        
        # Read execution setting info from ExecutionSetting.txt
        file_path = os.path.dirname(setting.__file__)
        f_read = open(file_path + "\\ExecutionSetting.txt", "r")
        line = f_read.readline()
        execution_setting_file_name = line.replace(end_line, "")
        f_read.close()

        # Read file and put to array
        f_stream = open(file_path + "\\" + execution_setting_file_name, "r")
        lines = f_stream.readlines()
        f_stream.close()
        
        # Get values
        items = []
        for i in range (0, len(lines)):
            lines[i] = lines[i].replace(end_line, "")
            items = lines[i].split(delim)
            if (len(items) == 2):
                if (items[0] == "browser_name"):
                    driverSetting.browser_name = items[1]
                elif (items[0] == "element_wait_timeout"):
                    driverSetting.element_wait_timeout = int(items[1])
                elif (items[0] == "hub_url"):
                    if (items[1] == "None"):
                        driverSetting.hub_url = None
                    else:
                        driverSetting.hub_url = items[1]
                elif (items[0] == "platform"):
                    driverSetting.platform = items[1]

        return driverSetting
    