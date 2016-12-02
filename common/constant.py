'''
Created on May 30, 2016

@author: thanh.viet.le
'''

class Constant(object):
    RunEnvironmentFile = "../data/RunEnv.txt"
    SuitableTechURL = "https://staging.suitabletech.com"
    AdminUsername = "tam.pham@logigear.com"
    AdminPassword = "Logigear123"
    DeviceGroup = "POC Devices"
    BeamPlusName = "QA BeamPlus Visitor1"
    BeamProNameUTF8 = u"QA BeamPro \u00a9 Visitor1"
    OrganizationName = "LogiGear Test"    
    WelcomeEmailTitle = "Welcome to Beam at " + OrganizationName
    WelcomeEmailContent = "Your Account | Support\nWelcome to Beam at LogiGear Test\nTam Pham invited you to Beam into LogiGear Test.\nTo get started, click this link to activate your account and set a password.\n\nActivate account\n\nThis link expires in 7 days.\nYour username is your email address: {}\nHave questions? Simply reply to this email or visit our support site.\nYou can change your email notification settings here.\nSuitable Technologies, Inc.\n921 E Charleston Rd\nPalo Alto, CA 94303\n1-855-200-2326"
    RemoveFromGroupEmailTitle = "[Beam] You have been removed from " + DeviceGroup
    RemoveFromGroupEmailContent = "Your Account | Support\nYou have been removed from POC Devices\nTam Pham removed you from POC Devices.\nHave questions? Simply reply to this email or visit our support site.\nYou can change your email notification settings here.\nSuitable Technologies, Inc.\n921 E Charleston Rd\nPalo Alto, CA 94303\n1-855-200-2326"
    
class Browser(object):
    Firefox = "Firefox"
    IE = "IE"
    Chrome = "Chrome"
    Safari = "Safari"
	Edge = "Edge"
    
class Platform(object):
    WINDOWS = "WINDOWS"
    MAC = "MAC"
    ANY = "ANY"
    