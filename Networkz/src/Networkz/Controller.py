'''
Created on Jun 15, 2015

@author: graysomb
'''
from win32api import keybd_event
from win32api import VkKeyScan
import win32con
import time
class Controller(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
      '''
    def pressKeys(self,netOutput):
        #[w,a,s,d,e,space]
        start = time.clock()
        if round(netOutput[0]) == 1:
            keybd_event(VkKeyScan('w'),0,0,0)
        else:
            keybd_event(VkKeyScan('w'),0 ,win32con.KEYEVENTF_KEYUP ,0)

        if round(netOutput[1]) == 1:
            keybd_event(VkKeyScan('a'),0,0,0)
        else:
            keybd_event(VkKeyScan('a'),0 ,win32con.KEYEVENTF_KEYUP ,0)
    
        if round(netOutput[2]) == 1:
            keybd_event(VkKeyScan('s'),0,0,0)
        else:
            keybd_event(VkKeyScan('s'),0 ,win32con.KEYEVENTF_KEYUP ,0)
            
        if round(netOutput[3]) == 1:
            keybd_event(VkKeyScan('d'),0,0,0)
        else:
            keybd_event(VkKeyScan('d'),0 ,win32con.KEYEVENTF_KEYUP ,0)
            
        if round(netOutput[4]) == 1:
            keybd_event(VkKeyScan('e'),0,0,0)
        else:
            keybd_event(VkKeyScan('e'),0 ,win32con.KEYEVENTF_KEYUP ,0)
        
        if round(netOutput[5]) == 1:
            keybd_event(win32con.VK_SPACE,0,0,0)
        else:
            keybd_event(win32con.VK_SPACE,0 ,win32con.KEYEVENTF_KEYUP ,0)
        
        
            
        