'''
Created on Mar 25, 2015

@author: graysomb
'''
import numpy as np

class Neuron:
    '''
    classdocs
    '''


    def __init__(self, inpNum):
        
        self.inputNum = inpNum
        self.bias = np.random.normal(0,1,1)
        self.weights = np.random.normal(0,1,inpNum)
        
    def output(self,inp):
        s = 0
        for i in range(len(self.weights)):
            s = s+self.weights[i]*inp[i]
        return self.sigmoid(sum+self.bias)
    
    def sigmoid(self,num):
        ans = 1.0/(1+np.exp(-num))
        return ans
    
    def getWeights(self):
        return self.weights
    
    def getBias(self):
        return self.bias
            
            
        
        