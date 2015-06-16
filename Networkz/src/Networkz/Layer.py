'''
Created on Mar 26, 2015

@author: graysomb
'''
from Networkz import Neuron
import numpy as np

class Layer:
    '''
    classdocs
    '''


    def __init__(self, neuronNum, inputNum):
        
        self.neurons = []
        for i in range(neuronNum):
            self.neurons.append(Neuron.Neuron(inputNum))
            
        self.weightMatrix = []
        for i in range(neuronNum):
            self.weightMatrix.append(self.neurons[i].getWeights())
        
        self.biasVector = []
        for i in range(neuronNum):
            self.biasVector.append(self.neurons[i].getBias())
        self.learnRate = .9
    
    def computeOutput(self, inp):
        w = np.mat(self.weightMatrix)
        a = np.mat(inp)
        b = np.array(self.biasVector)
        ans = np.transpose(np.inner(w,a)+b)
        self.output = ans
        self.outputSig = self.sigmoid(ans)
        return self.outputSig
    
    def updateBiases(self,error):
        self.biasVector = self.biasVector - self.learnRate*error
        ''' add stuff to update neurons'''
        
    def updateWeights(self,error):
        self.weightMatrix = self.weightMatrix - self.learnRate*error
    ''' add stuff to update neurons'''
        
    def sigmoid(self,num):
        ans = 1.0/(1+np.exp(-num))
        return ans
    
    def sigmoidP(self,num):
        ans = np.exp(-num)/((1+np.exp(-num))^2)
        return ans
    
    def getNeurons(self):
        return self.neurons
    
    def getOutput(self):
        return self.output
    
    def getOutputSig(self):
        return self.outputSig
    def getWeightMatrix(self):
        return self.weightMatrix