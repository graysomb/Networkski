'''
Created on Jun 8, 2015

@author: graysomb
'''
import numpy as np
import scipy.misc as spmisc
from PIL.ImageGrab import grab
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from multiprocessing import Queue
from macpath import join

class Recorder(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Generates the list to record the data
        TODO change this fucking shit to return statements
        '''


        
    def recordVid(self, tLeng, output):
        '''
        Records screen and resizes to an array to self.vid over a specified time in seconds
        '''
        start = time.clock()
        L=[]
        vid = []
        for i in range(tLeng):
            time.sleep(1)
            l = grab()
            l= spmisc.imresize(l, .075, 'nearest')
            L.append([plt.imshow(l)])
            s = l.shape[0]*l.shape[1]*l.shape[2]
            lp=np.reshape(l, (1,s))
            vid.append(lp)
        dt = time.clock() - start
        output.put([vid,L,dt])
        print "viddone"
        output.task_done()

    def recordKeys(self, totalTime, output):
        
        '''
        Records key press events in a continous loop and records the time of the event 
        '''
        import pythoncom, pyHook
        wList = []
        aList = []
        sList = []
        dList = []
        spaceList = []
        eList = []
        start = time.clock()
        def OnKeyboardEvent(event):
#             print 'MessageName:',event.MessageName
#             print 'Message:',event.Message
#             print 'Time:',event.Time
#             print 'Window:',event.Window
#             print 'WindowName:',event.WindowName
#             print 'Ascii:', event.Ascii, chr(event.Ascii)
#             print 'Key:', event.Key
#             print 'KeyID:', event.KeyID
#             print 'ScanCode:', event.ScanCode
#             print 'Extended:', event.Extended
#             print 'Injected:', event.Injected
#             print 'Alt', event.Alt
#             print 'Transition', event.Transition
#             print '---'
            event.Key
            if event.Key == "W":
                wList.append(time.clock()-start)
            if event.Key == "A":
                aList.append(time.clock()-start)
            if event.Key == "S":
                sList.append(time.clock()-start)
            if event.Key == "D":
                dList.append(time.clock()-start)
            if event.Key == "Space":
                spaceList.append(time.clock()-start)
            if event.Key == "E":
                eList.append(time.clock()-start)
            # return True to pass the event to other handlers
            
            return True

        # create a hook manager
        hm = pyHook.HookManager()
        # watch for all mouse events
        hm.KeyDown = OnKeyboardEvent
        # set the hook
        hm.HookKeyboard()
        # wait forever
        
        while time.clock()-start<totalTime+1.5:
            pythoncom.PumpWaitingMessages()
            
        output.put([wList,aList,sList,dList,eList,spaceList])
        print "keydone"
        output.task_done()
    def recordMouse(self,totalTime, output):
        
        '''
        records mouse events and their time and the position for mouse movements.
        '''
        MLD = []
        MLUp = []
        MRD =[]
        MRUp = []
        mMT = []
        mMP = []
        import pythoncom, pyHook
        start = time.clock()
        def OnMouseEvent(event):
            # called when mouse events are received
#             print 'MessageName:',event.MessageName
#             print 'Message:',event.Message
#             print 'Time:',event.Time
#             print 'Window:',event.Window
#             print 'WindowName:',event.WindowName
#             print 'Position:',event.Position
#             print 'Wheel:',event.Wheel
#             print 'Injected:',event.Injected
#             print '---'
            event.MessageName
            if event.MessageName == "mouse left down":
                MLD.append(time.clock()-start)
            if event.MessageName == "mouse left up":
                MLUp.append(time.clock()-start)
            if event.MessageName == "mouse right down":
                MRD.append(time.clock()-start)
            if event.MessageName == "mouse right up":
                MRUp.append(time.clock()-start)
            if event.MessageName == "mouse move":
                mMT.append(time.clock()-start)
                mMP.append(event.Position)
                
            

            # return True to pass the event to other handlers
            return True

        # create a hook manager
        hm = pyHook.HookManager()
        # watch for all mouse events
        hm.MouseAll = OnMouseEvent
        # set the hook
        hm.HookMouse()
        # wait forever
        while time.clock()-start<totalTime+1:
            pythoncom.PumpWaitingMessages()
            
        output.put([MLD,MLUp,MRD,MRUp,mMT,mMP])
        print "mousedone"
        output.task_done()
        
    def getLists(self, name):
        '''
        returns the lists of times or posistions upon request.
        '''
        if name == "w":
            return self.wList
        if  name == "a":
            return self.aList
        if name == "d":
            return self.dList
        if name == "s":
            return self.sList
        if name == "e":
            return self.eList
        if name == "space":
            return self.spaceList
        if name == "mlup":
            return self.MLUp
        if name == "mld":
            return self.MLD
        if name == "mrup":
            return self.MRUp
        if name == "mrd":
            return self.MRUp
        if name == "mM":
            return [self.mMt,self.mMP]
        if name == "vid":
            return self.vid
        if name == "keyList":
            return [self.wList,self.aList,self.sList,self.dList,self.eList,self.spaceList]
        if name == "mouseList":
            return [self.MLD,self.MLUp,self.MRD,self.MRUp,self.mMT,self.mMP]
            
            
            
            
        

    