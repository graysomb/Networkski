'''
Created on Mar 26, 2015

@author: graysomb
'''
from Networkz import Layer
import numpy as np
class Network:
    '''
    classdocs
    '''


    def __init__(self, layerNum, neuronNum, inputNum):
        self.layers = []
        self.map = [layerNum, neuronNum, inputNum]
        for i in range(layerNum):
            self.layers.append(Layer.Layer(neuronNum[i],inputNum[i]))
        
    def propogate(self,inp):
        current = inp
        for layer in self.layers:
            nex = layer.computeOutput(current)
            current = nex
        return current
            
    def backPropogate(self, trainOutput,inp):
        layerNum =len(self.layers)
        a = self.layers[layerNum-1].getOutputSig()
        z = self.layers[layerNum-1].getOutput()
        error = []
        error.append( np.transpose(np.multiply((a-trainOutput),self.sigmoidP(z))))
        
        '''Generate deltas for each layer'''
        for i in range(layerNum-1):
            w = self.layers[layerNum-1-(i)].getWeightMatrix()
            z = self.layers[layerNum-1-(i+1)].getOutput()
            '''
            not sure if this is right try this first if not learning'''
            e = np.transpose(error[i])
            if(e.shape[0] != 1):
                e = np.transpose(e)
            inter = np.inner(np.transpose(w),e)
            error.append( np.multiply(inter,np.transpose(self.sigmoidP(z))))
            
        ''' update weights and biases in each layer'''
        for i in range(layerNum):
            e = np.transpose(error[i])
            if(e.shape[1] != 1):
                e = np.transpose(e)
            self.layers[layerNum-1-i].updateBiases(error[i])
            if(layerNum-2-i<0):
                alm1 = inp
            else:
                alm1 = self.layers[layerNum-2-i].getOutputSig()
                
            dw = np.outer(error[i],alm1)
            self.layers[layerNum-1-i].updateWeights(dw)
                           
    def sigmoidP(self,num):
        ans1 = np.multiply((1+np.exp(-num)),(1+np.exp(-num)))
        ans2 = np.divide(np.exp(-num),ans1)
        return ans2
        
        