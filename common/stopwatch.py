'''
Created on May 31, 2016

@author: thanh.viet.le
'''

import datetime

class Stopwatch(object):

    def __init__(self):
        pass
    
    def _now(self):
        return datetime.datetime.now()
    
    def start(self):
        self.start = self._now()
        return self.start
    
    def stop(self):        
        pass
    
    def elapsed(self):
        return (self._now() - self.start)
		
	def van_test(self):
		pass
    
	def van2(self):
		pass
		
    def van1(self):
		pass
		
	def testsetset(self):
		pass