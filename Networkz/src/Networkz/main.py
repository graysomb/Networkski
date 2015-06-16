'''
Created on Mar 26, 2015

@author: graysomb
'''
from Networkz import Network, Recorder, RecThreader, Controller
import time
import scipy as sp
import numpy as np
import scipy.misc as spmisc
from PIL.ImageGrab import grab
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
from matplotlib.cbook import Null
from Networkz import RecThreader
from multiprocessing import Process



if __name__ == '__main__':
#     r = RecThreader.RecThreader()
#     r.record(2)
#     r.GenerateSamples()
#     r.saveIO()
    c = Controller.Controller()
    c.pressKeys()
    
    
    
    
    '''
    import time
    start = time.clock()
    L=[]
    for i in range(100):
        l = grab()
        l = spmisc.imresize(l, .05, 'nearest')
        L.append([plt.imshow(l)])
        s=l.shape[0]*l.shape[1]*l.shape[2]
        lp = np.reshape(l, (1,s))
        lp = np.divide(lp,256)
    layerNum = 5
    neuronNum = [100,50,25,12,9]
    inputNum = [s,100,50,25,12]
    newNetwork = Network.Network(layerNum, neuronNum, inputNum)
    a = []
    for i in range(100):
        ans=newNetwork.propogate(lp)
        print "Ouput: "
        print i 
        print "ans: "
        print ans
        print "done"
        a.append(i)
        a.append(ans)
        newNetwork.backPropogate([1,0,0,0,0,0,0,0,0],lp)
        print "done back"
        
    end = time.clock()
    print end- start
    '''
    
    
    '''
    import time
    L=[]
    for i in range(40):
        time.sleep(1)
        l = grab()
        l= spmisc.imresize(l, .075, 'nearest')
        L.append([plt.imshow(l)])
    
    fig = plt.figure()
    ani = animation.ArtistAnimation(fig, L, interval=50, blit=True,
    repeat_delay=1000)
    plt.show()
    print l.shape
    print l.shape[0]*l.shape[1]*l.shape[2]
    s = l.shape[0]*l.shape[1]*l.shape[2]
    lp=np.reshape(l, (1,s))
    
    print lp
    '''
    
    '''
    import pythoncom, pyHook

    def OnKeyboardEvent(event):
        print 'MessageName:',event.MessageName
        print 'Message:',event.Message
        print 'Time:',event.Time
        print 'Window:',event.Window
        print 'WindowName:',event.WindowName
        print 'Ascii:', event.Ascii, chr(event.Ascii)
        print 'Key:', event.Key
        print 'KeyID:', event.KeyID
        print 'ScanCode:', event.ScanCode
        print 'Extended:', event.Extended
        print 'Injected:', event.Injected
        print 'Alt', event.Alt
        print 'Transition', event.Transition
        print '---'

    # return True to pass the event to other handlers
        return True

    # create a hook manaasger
    hm = pyHook.HookManager()
    # watch for all mouse eventsa
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()
    '''
    '''
    import pythoncom, pyHook
    def OnMouseEvent(event):
        # called when mouse events are received
        print 'MessageName:',event.MessageName
        print 'Message:',event.Message
        print 'Time:',event.Time
        print 'Window:',event.Window
        print 'WindowName:',event.WindowName
        print 'Position:',event.Position
        print 'Wheel:',event.Wheel
        print 'Injected:',event.Injected
        print '---'

        # return True to pass the event to other handlers
        return True

    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.MouseAll = OnMouseEvent
    # set the hook
    hm.HookMouse()
    # wait forever
    pythoncom.PumpMessages()    
'''
    
    
    
    
    
    '''
    TODO minecraft bot
    
    keypress monitoring
    
    turn learning on and off via action listeners
    
    run minecraft in small window
    
    input:
    [image, most recent button vector, last image?, last button vector?]
    or 
    [image, most recent button vector, last output]
    since output is small could use 
    
    
    button vector(boolean):
    [W,A,S,D,left click, right click, space]
    
    
    Learning method
    observational
    input important past changes in button vector
    check if output equal observed and change learing rate accordingly. i.e suprise
    
    '''
    
    

